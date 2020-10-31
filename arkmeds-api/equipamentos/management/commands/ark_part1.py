import os

from django.core.management.base import BaseCommand, CommandError
from services.arkmeds_services import Services
import random
import time


class Command(BaseCommand):
    help = 'Consulta equipamentos'

    def __init__(self):
        self.services = Services(
            os.getenv('ARKMEDS_USER', 'testedev@arkmeds.com'),
            os.getenv('ARKMEDS_PASSWORD', 'testedev')
        )

    def faker_observation(self):
        observation = ''
        dictionary = ['neque', 'porro', 'quisquam', 'est',
                      'qui', 'dolorem', 'ipsum', 'quia', 'dolor',
                      'sit', 'amet', 'consectetur', 'adipisci', 'velit']
        for _ in range(random.randint(1, 100)):
            observation += random.choice(dictionary) + ' '
        return observation

    def fetch_companies(self, max_number=1):
        error, info, res = self.services.listar_empresas()
        if error:
            raise CommandError(info)
        return res.json()[:max_number]

    def fetch_company_detail(self, company_id):
        error, info, res = self.services.empresa_detalhada(company_id)
        if error:
            raise CommandError(info)
        return res.json()

    def open_ticket(self, equipment):
        equipment = equipment['id']
        solicitante = equipment['proprietario']['id']
        tipo_servico = 3
        problema = 5
        observacoes = self.faker_problem()
        data_criacao = int((time.time() + 0.5) * 1000)
        id_tipo_ordem_servico = 1
        error, info, res = self.services.criar_chamado(
            equipment, solicitante, tipo_servico, problema,
            observacoes, data_criacao, id_tipo_ordem_servico)
        if error:
            raise CommandError(info)
        return res.json()

    def map_company_ids(self, companies=[]):
        return [company['id'] for company in companies]

    def fetch_equipamentos(self, company_id, page=1):
        error, info, res = self.services.equipamentos_por_empresas(
            id=company_id, page=page)
        if error:
            raise CommandError(info)
        response = res.json()
        has_next = response['next'] is not None
        return has_next, response['results']

    def equipments(self, company_id):
        equipamentos = []
        page = 1
        has_next, results = self.fetch_equipamentos(company_id, page)
        equipamentos.append(results)
        while has_next:
            page += 1
            has_next, results = self.fetch_equipamentos(company_id, page)
            equipamentos.append(results)
        return equipamentos

    def is_type_5(self, detailed_company):
        return detailed_company['id'] == '5'

    def companies_details_excluding_type_5(self, companies):
        detailed_companies = []
        for company_id in self.map_company_ids(companies):
            detailed_company = self.fetch_company_detail(company_id)
            if self.is_type_5(detailed_company):
                continue
            detailed_companies.append(detailed_company)
        return detailed_companies

    def equipments_from_companies(self, detailed_company):
        equipments = []
        for company_id in self.map_company_ids(detailed_company):
            equipment = self.equipments(company_id)
            equipments.append(equipment)
        return equipments

    def open_ticket_for_equipments(self, equipments):
        for equipment in equipments:
            self.open_ticket(equipment)

    def handle(self, *args, **options):
        companies = self.fetch_companies(max_number=20)
        # Part1
        detailed_companies = self.companies_details_excluding_type_5(companies)
        # Part2
        equipments = self.equipments_from_companies(detailed_companies)
        # Part3
        self.open_ticket_for_equipments(equipments)

import os
import random
import time

from django.core.management.base import BaseCommand, CommandError
from equipamentos.models import (ChamadoEquipamento, Empresa, Equipamento,
                                 Proprietario, ResponsavelTecnico,
                                 TipoEquipamento)
from services.arkmeds_services import Services


class Command(BaseCommand):
    help = 'Consulta equipamentos'

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.services = Services(
            os.getenv('ARKMEDS_USER', 'testedev@arkmeds.com'),
            os.getenv('ARKMEDS_PASSWORD', 'testedev')
        )
        self.already_imported_companies = self.get_already_imported_companies()
        self.already_imported_equipments = self.get_already_imported_equipments()
        self.already_imported_tickets = self.get_already_imported_tickets()

    def faker_observation(self):
        observation = ''
        dictionary = ['neque', 'porro', 'quisquam', 'est',
                      'qui', 'dolorem', 'ipsum', 'quia', 'dolor',
                      'sit', 'amet', 'consectetur', 'adipisci', 'velit']
        for _ in range(random.randint(1, 100)):
            observation += random.choice(dictionary) + ' '
        return observation

    def get_already_imported_companies(self):
        return Empresa.objects.all().values_list('id', flat=True)

    def get_already_imported_equipments(self):
        return Equipamento.objects.all().values_list('id', flat=True)

    def get_already_imported_tickets(self):
        return ChamadoEquipamento.objects.all().values_list('id', flat=True)

    def fetch_companies(self, max_number=1):
        self.stdout.write(self.style.SUCCESS('[+]Fetching companies'))
        error, info, res = self.services.listar_empresas()
        if error:
            raise CommandError(info)
        total_fetched = len(res.json())
        self.stdout.write(self.style.SUCCESS(f'Total fetched {total_fetched}'))
        selected_companies = len(res.json()[:max_number])
        self.stdout.write(self.style.SUCCESS(
            f'Selected companies {selected_companies}'))
        return res.json()[:max_number]

    def fetch_company_detail(self, company_id):
        error, info, res = self.services.empresa_detalhada(company_id)
        if error:
            raise CommandError(info)
        return res.json()

    def open_ticket(self, equip):
        equipment = equip['id']
        solicitante = equip['proprietario']['id']
        tipo_servico = 3
        problema = 5
        observacoes = self.faker_observation()
        data_criacao = int((time.time() + 0.5) * 1000)
        id_tipo_ordem_servico = 1
        error, info, res = self.services.criar_chamado(
            equipment, solicitante, tipo_servico, problema,
            observacoes, data_criacao, id_tipo_ordem_servico
        )
        if error:
            raise CommandError(info)
        return res.json()

    def map_company_ids(self, companies=[]):
        return [company['id'] for company in companies]

    def map_equipments_ids(self, equipments=[]):
        return [equipment['id'] for equipment in equipments]

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
        equipamentos.extend(results)
        while has_next:
            page += 1
            has_next, results = self.fetch_equipamentos(company_id, page)
            equipamentos.extend(results)
        return equipamentos

    def fetch_tickets(self, equipment_id, page=1):
        error, info, res = self.services.chamado_por_equipamento(
            id=equipment_id, page=page)
        if error:
            raise CommandError(info)
        response = res.json()
        has_next = response['next'] is not None
        return has_next, response['results']

    def tickets(self, equipment_id):
        tickets = []
        page = 1
        has_next, results = self.fetch_tickets(equipment_id, page)
        tickets.extend(results)
        while has_next:
            page += 1
            has_next, results = self.fetch_tickets(equipment_id, page)
            tickets.extend(results)
        return tickets

    def is_type_5(self, detailed_company):
        return detailed_company['id'] == '5'

    def companies_details_excluding_type_5(self, companies):
        self.stdout.write(self.style.SUCCESS(
            '[+]Fetching companies details excluding type 5'))
        detailed_companies = []
        for company_id in self.map_company_ids(companies):
            detailed_company = self.fetch_company_detail(company_id)
            if self.is_type_5(detailed_company):
                continue
            detailed_companies.append(detailed_company)
        total_fetched = len(detailed_companies)
        self.stdout.write(self.style.SUCCESS(f'Total fetched {total_fetched}'))
        return detailed_companies

    def equipments_from_companies(self, detailed_company):
        self.stdout.write(self.style.SUCCESS(
            '[+]Fetching equipments from companies'))
        equipments = []
        for company_id in self.map_company_ids(detailed_company):
            equipment = self.equipments(company_id)
            equipments.extend(equipment)
        total_fetched = len(equipments)
        self.stdout.write(self.style.SUCCESS(f'Total fetched {total_fetched}'))
        return equipments

    def open_ticket_for_equipments(self, equipments):
        self.stdout.write(self.style.SUCCESS('[+]Opening tickets'))
        for equipment in equipments:
            self.open_ticket(equipment)

    def save_companies(self, companies):
        self.stdout.write(self.style.SUCCESS('[+]Importing companies'))
        obj_companies = []
        already_imported = 0
        for company in companies:
            if company['id'] not in self.already_imported_companies:
                empresa_detalhe = Empresa(
                    id=company['id'],
                    tipo=company['tipo'],
                    nome=company['nome_fantasia'],
                    nome_fantasia=company['nome_fantasia'],
                    superior=company['superior'],
                    cnpj=company['cnpj'],
                    observacoes=company['observacoes'],
                    contato=company['contato'],
                    email=company['email'],
                    telefone1=company['telefone1'],
                    ramal1=company['ramal1'],
                    telefone2=company['telefone2'],
                    ramal2=company['ramal2'],
                    fax=company['fax'],
                    cep=company['cep'],
                    rua=company['rua'],
                    numero=company['numero'],
                    bairro=company['bairro'],
                    cidade=company['cidade'],
                    estado=company['estado'],
                )
                obj_companies.append(empresa_detalhe)
            else:
                already_imported += 1
        if already_imported > 0:
            self.stdout.write(self.style.SUCCESS(
                f'{already_imported} companies already imported'))
        Empresa.objects.bulk_create(obj_companies)
        new_imported = len(obj_companies)
        self.stdout.write(self.style.SUCCESS(
            f'{new_imported} new companies imported'))

    def get_or_create_proprietary(self, equipment):
        id = equipment['proprietario']['id']
        nome = equipment['proprietario']['nome']
        apelido = equipment['proprietario']['apelido']
        proprietary, created = Proprietario.objects.get_or_create(id=id, defaults={'id': id, 'nome': nome, 'apelido': apelido})
        return proprietary

    def get_or_create_equipment_tipo(self, equipment):
        id = equipment['tipo']['id']
        descricao = equipment['tipo']['descricao']
        equipment_type, created = TipoEquipamento.objects.get_or_create(id=id, defaults={'id': id, 'descricao': descricao})
        return equipment_type

    def get_or_create_resp_tecnico(self, ticket):
        has_resp_tecnico = ticket['get_resp_tecnico']['has_resp_tecnico']
        if has_resp_tecnico:
            id = ticket['get_resp_tecnico']['id']
            has_avatar = ticket['get_resp_tecnico']['has_avatar']
            nome = ticket['get_resp_tecnico']['nome']
            email = ticket['get_resp_tecnico']['email']
            has_resp_tecnico = has_resp_tecnico
            avatar = ticket['get_resp_tecnico']['avatar']
            get_resp_tecnico, created = ResponsavelTecnico.objects.get_or_create(id=id, defaults={'id': id, 'nome': nome, 'email': email, 'has_avatar': has_avatar, 'has_resp_tecnico': has_resp_tecnico, 'avatar': avatar})
        else:
            get_resp_tecnico = None

        return get_resp_tecnico

    def save_equipments(self, equipments):
        self.stdout.write(self.style.SUCCESS('[+]Importing equipments'))
        obj_equipments = []
        already_imported = 0
        for equipment in equipments:
            if equipment['id'] not in self.already_imported_equipments:
                proprietary = self.get_or_create_proprietary(equipment)
                equipment_type = self.get_or_create_equipment_tipo(equipment)
                equipment = Equipamento(
                    id=equipment['id'],
                    fabricante=equipment['fabricante'],
                    modelo=equipment['modelo'],
                    patrimonio=equipment['patrimonio'],
                    numero_serie=equipment['numero_serie'],
                    identificacao=equipment['identificacao'],
                    proprietario=proprietary,
                    tipo=equipment_type,
                    qr_code=equipment['qr_code'],
                )
                obj_equipments.append(equipment)
            else:
                already_imported += 1
        if already_imported > 0:
            self.stdout.write(self.style.SUCCESS(
                f'{already_imported} equipments already imported'))
        new_imported = len(obj_equipments)
        self.stdout.write(self.style.SUCCESS(
            f'{new_imported} new equipments imported'))
        Equipamento.objects.bulk_create(obj_equipments)

    def get_tickets_from_all_equipments(self, equipments):
        self.stdout.write(self.style.SUCCESS('[+]Importing tickets'))
        all_tickets = []
        already_imported = 0
        for equipment_id in self.map_equipments_ids(equipments):
            tickets = self.tickets(equipment_id)
            for ticket in tickets:
                if ticket['id'] not in self.already_imported_tickets:
                    resp_tecnico = self.get_or_create_resp_tecnico(ticket)
                    ticket_obj = ChamadoEquipamento(
                        id=ticket['id'],
                        chamados=ticket['chamados'],
                        cor_prioridade=ticket['cor_prioridade'],
                        prioridade=ticket['prioridade'],
                        get_prioridade=ticket['get_prioridade'],
                        numero=ticket['numero'],
                        get_solicitante=ticket['get_solicitante'],
                        get_equipamento_servico=ticket['get_equipamento_servico'],
                        get_criticidde=ticket['get_criticidde'],
                        tempo=ticket['tempo'],
                        tempo_fechamento=ticket['tempo_fechamento'],
                        responsavel_str=ticket['responsavel_str'],
                        get_resp_tecnico=resp_tecnico,
                        problema_str=ticket['problema_str'],
                        chamado_arquivado=ticket['chamado_arquivado'],
                        estado=ticket['estado'],
                        equipamento_id=equipment_id,
                    )
                    all_tickets.append(ticket_obj)
                else:
                    already_imported += 1
        if already_imported > 0:
            self.stdout.write(self.style.SUCCESS(f'{already_imported} tickets already imported'))
        new_imported = len(all_tickets)
        ChamadoEquipamento.objects.bulk_create(all_tickets)
        self.stdout.write(self.style.SUCCESS(f'{new_imported} new tickets imported'))


    def handle(self, *args, **options):
        # Part 1
        companies = self.fetch_companies(max_number=20)
        detailed_companies = self.companies_details_excluding_type_5(companies)
        equipments = self.equipments_from_companies(detailed_companies)
        self.open_ticket_for_equipments(equipments)
        # Part2
        self.save_companies(detailed_companies)
        self.save_equipments(equipments)
        self.get_tickets_from_all_equipments(equipments)

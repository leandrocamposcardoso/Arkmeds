import os

from django.core.management.base import BaseCommand, CommandError
from equipamentos.models import (Chamado, Detalhe, Empresa, Equipamento,
                                 TipoDetalhe, Proprietario, TipoEquipamento)
from services.arkmeds_services import Services


class Command(BaseCommand):
    help = 'Inserting data from API to Postgres database'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('[+]initializing service'))
        user = os.getenv('ARKMEDS_USER', 'testedev@arkmeds.com')
        password = os.getenv('ARKMEDS_PASSWORD', 'testedev')
        service = Services(user, password)
        if not service.token:
            raise CommandError(
                'Authentication error, failed to retreive token')
        self.stdout.write(self.style.SUCCESS('[+]Retrieving companies'))
        error, info, res = service.listar_empresas()
        if error:
            raise CommandError(info)
        json_companies = res.json()
        self.stdout.write(self.style.SUCCESS(
            '[+]Selecting first 20 companies'))
        companies = json_companies[:20]
        self.stdout.write(self.style.SUCCESS('[+]Importing companies...'))
        already_imported = Empresa.objects.all().values_list('id', flat=True)
        for company in companies:
            id = company['id']
            nome = company['nome']
            apelido = company['apelido']
            empresa = None
            if id in already_imported:
                self.stdout.write(self.style.ERROR(
                    f'[!]Company {nome} alredy imported!'))
            else:
                self.stdout.write(self.style.SUCCESS(
                    f'[+]Company {nome} imported!'))
                empresa = Empresa(id, nome, apelido).save()
                self.stdout.write(self.style.SUCCESS('[+]Getting details'))
                error, info, res = service.empresa_detalhada(id)
                if error:
                    raise CommandError(info)
                detailed_company = res.json()
                tipo = TipoDetalhe.objects.get_or_create(id=id)[0]
                self.stdout.write(self.style.SUCCESS('[+]Importing details'))
                Detalhe.objects.create(
                    id=id,
                    empresa=empresa,
                    tipo=tipo,
                    nome=nome,
                    nome_fantasia=apelido,
                    superior=detailed_company['superior'],
                    cnpj=detailed_company['cnpj'],
                    observacoes=detailed_company['observacoes'],
                    contato=detailed_company['contato'],
                    email=detailed_company['email'],
                    telefone1=detailed_company['telefone1'],
                    ramal1=detailed_company['ramal1'],
                    telefone2=detailed_company['telefone2'],
                    ramal2=detailed_company['ramal2'],
                    fax=detailed_company['fax'],
                    cep=detailed_company['cep'],
                    rua=detailed_company['rua'],
                    numero=detailed_company['numero'],
                    bairro=detailed_company['bairro'],
                    cidade=detailed_company['cidade'],
                    estado=detailed_company['estado'],
                )
            self.stdout.write(self.style.SUCCESS('[+]Receiving equipments'))
            error, info, res = service.equipamentos_por_empresas(id=id)
            if error:
                raise CommandError(info)
            equipamentos = res.json()['results']
            self.stdout.write(self.style.SUCCESS('[+]Importing equipments'))
            for equipamento in equipamentos:
                self.stdout.write(self.style.SUCCESS(f'[+]Creating owner'))
                proprietario = Proprietario.objects.get_or_create(
                    id=equipamento['proprietario']['id'],
                    nome=equipamento['proprietario']['nome'],
                    apelido=equipamento['proprietario']['apelido'],
                )[0]
                self.stdout.write(self.style.SUCCESS(f'[+]Creating type'))
                tipo = TipoEquipamento.objects.get_or_create(
                    id=equipamento['tipo']['id'],
                    descricao=equipamento['tipo']['descricao'],
                )[0]
                self.stdout.write(self.style.SUCCESS('[+]Importing equipment'))
                equipamentos = Equipamento.objects.get_or_create(
                    id=equipamento['id'],
                    fabricante=equipamento['fabricante'],
                    modelo=equipamento['modelo'],
                    patrimonio=equipamento['patrimonio'],
                    numero_serie=equipamento['numero_serie'],
                    identificacao=equipamento['identificacao'],
                    proprietario=proprietario,
                    tipo=tipo,
                    qr_code=equipamento['qr_code'],
                )[0]

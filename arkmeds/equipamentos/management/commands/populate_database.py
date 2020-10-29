from django.core.management.base import BaseCommand, CommandError
from services.arkmeds_services import Services
import os


class Command(BaseCommand):
    help = 'Inserting data from API to Postgres database'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('[+]initializing service'))
        user = os.getenv('ARKMEDS_USER', 'testedev@arkmeds.com')
        password = os.getenv('ARKMEDS_PASSWORD', 'password')
        service = Services(user, password)
        if not service.token:
            raise CommandError('Authentication error, failed to retreive token')
        self.stdout.write(self.style.SUCCESS('[+]Retrieving companies'))
        error, info, res = service.listar_empresas()
        if error:
            raise CommandError(info)
        json_companies = res.json()

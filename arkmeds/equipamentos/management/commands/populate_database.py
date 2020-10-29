from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Inserting data from API to Postgres database'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('[+]Recebendo empresas'))

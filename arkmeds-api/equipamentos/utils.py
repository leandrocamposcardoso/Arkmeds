from services.arkmeds_services import Services
from django.core.management.base import CommandError


class CommandPipeline:
    def __init__(self, user, password):
        self.service = Services(user, password)
        if not self.service.token:
            raise CommandError('Authentication fail')

from django.core.management import BaseCommand
from myapp2.models import Client

class Command(BaseCommand):
    help = "Get client."

    def add_arguments(self, parser):
        parser.add_argument('id', type =int, help = "id")

    def handle(self, *args, **kwargs):
        client = Client.objects.filter(pk = kwargs['id']).first()
        self.stdout.write(f'{client}')
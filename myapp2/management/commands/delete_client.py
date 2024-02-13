from django.core.management import BaseCommand
from myapp2.models import Client

class Command(BaseCommand):
    help = "Delete client."

    def add_arguments(self, parser):
        parser.add_argument('id', type =int, help = "id")

    def handle(self, *args, **kwargs):
        client = Client.objects.filter(pk = kwargs['id']).first()
        if client is not None:
            client.delete()
        self.stdout.write(f'{client}')
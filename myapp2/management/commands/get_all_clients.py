from django.core.management import BaseCommand
from myapp2.models import Client

class Command(BaseCommand):
    help = "Get all clients."

    def handle(self, *args, **options):
        clients = Client.objects.all()
        self.stdout.write(f'{clients}')

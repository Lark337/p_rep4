from django.core.management import BaseCommand
from myapp2.models import Client

class Command(BaseCommand):
    help = "Create client."

    def add_arguments(self, parser):
        parser.add_argument('name', type =str, help = "name")
        parser.add_argument('email', type =str, help = "email")
        parser.add_argument('phone_number', type= int, help = "phone_number")
        parser.add_argument('address', type =str, help = "address")

    def handle(self, *args, **kwargs):
        client = Client(name = kwargs['name'] , email = kwargs['email'], phone_number = kwargs['phone_number'],address = kwargs['address'])
        client.save()
        self.stdout.write(f'{client}')

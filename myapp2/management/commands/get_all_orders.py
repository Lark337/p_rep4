from django.core.management import BaseCommand
from myapp2.models import Client
from myapp2.models import Product
from myapp2.models import Order


class Command(BaseCommand):
    help = "Get all orders."

    def handle(self, *args, **options):
        orders = Order.objects.all()
        self.stdout.write(f'{orders}')
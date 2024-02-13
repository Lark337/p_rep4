from decimal import Decimal

from django.core.management import BaseCommand
from myapp2.models import Product

class Command(BaseCommand):
    help = "Create product."

    def add_arguments(self, parser):
        parser.add_argument('name', type =str, help = "name")
        parser.add_argument('description', type =str, help = "description")
        parser.add_argument('price', type= Decimal, help = "price")
        parser.add_argument('amount', type =int, help = "amount")

    def handle(self, *args, **kwargs):
        product = Product(name = kwargs['name'] , description = kwargs['description'], price = kwargs['price'],amount = kwargs['amount'])
        product.save()
        self.stdout.write(f'{product}')

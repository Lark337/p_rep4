from django.core.management import BaseCommand
from myapp2.models import Product
from decimal import Decimal

class Command(BaseCommand):
    help = "Update product."

    def add_arguments(self, parser):
        parser.add_argument('id', type=int, help="id")
        parser.add_argument('name', type=str, help="name")
        parser.add_argument('description', type=str, help="description")
        parser.add_argument('price', type=Decimal, help="price")
        parser.add_argument('amount', type=int, help="amount")

    def handle(self, *args, **kwargs):
        product = Product.objects.filter(pk=kwargs['id']).first()
        product.name = kwargs['name']
        product.description = kwargs['description'],
        product.price = kwargs['price']
        product.amount = kwargs['amount']
        product.save()
        self.stdout.write(f'{product}')
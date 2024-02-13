from django.core.management import BaseCommand
from decimal import Decimal
from myapp2.models import Client
from myapp2.models import Product
from myapp2.models import Order

class Command(BaseCommand):
    help = "Create order."

    def add_arguments(self, parser):
        parser.add_argument('client_id', type =int, help = "client")
        parser.add_argument('product_id', type =int, help = "product")

    def handle(self, *args, **kwargs):
        if Order.objects.filter(client_id = kwargs['client_id']).first() is None:
            client = Client.objects.filter(pk = kwargs['client_id']).first()
            product = Product.objects.filter(pk = kwargs['product_id']).first()
            order = Order(client = client, total_price = Decimal(0))
            order.save()
            order.products.add(product)
            new_total_price = order.total_price + product.price
            order.total_price = new_total_price
            order.save()
        else:
            order = Order.objects.filter(client_id=kwargs['client_id']).first()
            product = Product.objects.filter(pk = kwargs['product_id']).first()
            new_total_price = order.total_price + product.price
            order.total_price = new_total_price
            order.products.add(product)
            order.save()

        self.stdout.write(f'{order}')
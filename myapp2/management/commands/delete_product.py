from django.core.management import BaseCommand
from myapp2.models import Product

class Command(BaseCommand):
    help = "Delete product."

    def add_arguments(self, parser):
        parser.add_argument('id', type =int, help = "id")

    def handle(self, *args, **kwargs):
        product = Product.objects.filter(pk = kwargs['id']).first()
        if product is not None:
            product.delete()
        self.stdout.write(f'{product}')
from django.core.management import BaseCommand
from myapp2.models import Product

class Command(BaseCommand):
    help = "Get all products."

    def handle(self, *args, **options):
        products = Product.objects.all()
        self.stdout.write(f'{products}')

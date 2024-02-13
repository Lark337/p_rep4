from django.core.management import BaseCommand
from myapp2.models import Order

class Command(BaseCommand):
    help = "Delete order."

    def add_arguments(self, parser):
        parser.add_argument('id', type =int, help = "id")

    def handle(self, *args, **kwargs):
        order = Order.objects.filter(pk = kwargs['id']).first()
        if order is not None:
            order.delete()
        self.stdout.write(f'{order}')
from django.db import models

# Create your models here.

from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    phone_number = models.IntegerField()
    address = models.CharField(max_length=50)
    registration_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return (f"Client: {self.name}, email: {self.email}, phone number: {self.phone_number} address: {self.address} "
                f"registration date: {self.registration_date}")

class Product(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    amount = models.IntegerField()
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return (f"Product: {self.name}, description: {self.description},price: {self.price} "
                f"amount: {self.amount}, date added: {self.date_added}")

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_ordered = models.DateField(auto_now_add=True)

    def __str__(self):
        return (f"Client: {self.client.name}, products: {Order.objects.get(client=self.client).products.all()},total_price = {self.total_price}, "
                f"date ordered: {self.date_ordered}")
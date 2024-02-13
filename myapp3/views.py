from django.shortcuts import render,get_object_or_404

from myapp2.models import Product,Client,Order

from .forms import ProductForm

# Create your views here.

def get_product(request,prodict_id):
    product = get_object_or_404(Product,pk = prodict_id)
    return render(request,'myapp3/get_product.html',{'product': product})

def get_products(request):
    products = Product.objects.all()
    return render(request,'myapp3/get_products.html', {'products': products})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        message = 'Ошибка'
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            amount = form.cleaned_data['amount']
            product = Product(name = name , description = description, price = price,amount = amount)
            product.save()
            message = "Product saved"
    else:
        form = ProductForm()
        message = 'Fill the form'
    return render(request,'myapp3/add_product.html',{'form': form, 'message': message})

def index(request):
    return render(request,'myapp3/index.html')

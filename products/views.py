from django.shortcuts import render
from .models import Product

# Create your views here.
def all_products(request):
    """ A view to show all products, including sorting and search queries """
    ''' This function will render the products.html template '''
    products = Product.objects.all()

    context = {
        'products': products,
    }
    
    return render(request, 'products/products.html', context)
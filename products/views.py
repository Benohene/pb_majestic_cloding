from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category

# Create your views here.
def all_products(request):
    """ A view to show all products, including sorting and search queries """
    ''' This function will render the products.html template '''
    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None
    

    if request.GET:
        # Sorting functionality
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))# This will sort the products by name in ascending order
            if sortkey == 'category':
                sortkey = 'category__name'
            if sortkey == 'price':
                sortkey = 'price'
            if sortkey == 'rating':
                sortkey = 'rating'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}' # This will sort the products by name in descending order
            products = products.order_by(sortkey)
            
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
        
        # Search functionality
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Your search cannot be found!")
                return redirect(reverse('products'))
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)
    
    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
        'current_direction': direction,      
    }
    
    
    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """
    ''' This function will render the product_detail.html template '''
    product = get_object_or_404(Product, pk=product_id)
    

         
    context = {
        'product': product,
    }
    
    return render(request, 'products/product_detail.html', context)
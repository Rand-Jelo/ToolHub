from django.shortcuts import render
from products.models import Product
from django.db.models import Q

def home(request):
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )
    else:
        products = Product.objects.all()

    return render(request, 'core/home.html', {'products': products})
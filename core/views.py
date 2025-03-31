from django.shortcuts import render
from products.models import Product, Tag
from django.db.models import Q
from products.filters import ProductFilter

def home(request):
    # Get all products
    products = Product.objects.all()
    
    # Get all tags for filtering
    tags = Tag.objects.all()
    
    # If a tag is selected, filter products by tag
    tag_id = request.GET.get('tag')
    if tag_id:
        products = products.filter(tags__id=tag_id)
    
    return render(request, 'core/home.html', {'products': products, 'tags': tags})
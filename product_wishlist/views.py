from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from products.models import Product
from .models import Wishlist

@login_required
def add_to_wishlist(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return redirect('product_list') 


    wishlist, created = Wishlist.objects.get_or_create(user=request.user)

   
    if product not in wishlist.items.all():
        wishlist.items.add(product)
        wishlist.save()

    return redirect('dashboard') 

@login_required
def view_wishlist(request):
    wishlist_items = Wishlist.objects.filter(user=request.user)
    return render(request, 'wishlist/wishlist.html', {'wishlist_items': wishlist_items})
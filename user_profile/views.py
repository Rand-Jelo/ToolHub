from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm
from orders.models import Order
from product_wishlist.models import Wishlist 

@login_required
def dashboard(request):
    orders = Order.objects.filter(user=request.user)

    try:
        wishlist = Wishlist.objects.get(user=request.user)
        wishlist_items = wishlist.items.all() 
    except Wishlist.DoesNotExist:
        wishlist_items = []

    return render(request, 'user_profile/dashboard.html', {
        'orders': orders,
        'wishlist_items': wishlist_items,
    })

@login_required
def profile_edit(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = UserChangeForm(instance=request.user)
    
    return render(request, 'user_profile/profile_edit.html', {'form': form})
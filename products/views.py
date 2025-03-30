from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from reviews.models import Review
from reviews.forms import ReviewForm
from product_wishlist.models import Wishlist

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    reviews = Review.objects.filter(product=product)
    has_reviewed = request.user.is_authenticated and Review.objects.filter(product=product, user=request.user).exists()

    # Wishlist handling
    has_in_wishlist = False
    if request.user.is_authenticated:
        has_in_wishlist = Wishlist.objects.filter(user=request.user, items=product).exists()

    if request.method == 'POST':
        if 'add_to_wishlist' in request.POST:
            wishlist, created = Wishlist.objects.get_or_create(user=request.user)
            if not has_in_wishlist:
                wishlist.items.add(product)
                has_in_wishlist = True
            else:
                wishlist.items.remove(product)
                has_in_wishlist = False 
            return redirect('product-detail', pk=pk)
        else:
            form = ReviewForm(request.POST)
            if form.is_valid():
                if not has_reviewed:
                    review = form.save(commit=False)
                    review.product = product
                    review.user = request.user
                    review.save()
                    return redirect('product-detail', pk=pk)
                else:
                    form.add_error(None, 'You have already reviewed this product.')
    else:
        form = ReviewForm()

    return render(request, 'products/product_detail.html', {
        'product': product,
        'reviews': reviews,
        'form': form,
        'has_reviewed': has_reviewed,
        'has_in_wishlist': has_in_wishlist
    })

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from reviews.models import Review
from reviews.forms import ReviewForm

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    reviews = Review.objects.filter(product=product)
    has_reviewed = request.user.is_authenticated and Review.objects.filter(product=product, user=request.user).exists()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            # Check if user already reviewed this product
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
        'has_reviewed': has_reviewed
    })
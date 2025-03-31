from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from products.models import Product
from .forms import ReviewForm
from .models import Review

@login_required
def add_review(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.product = product
            review.save()
            return redirect('product-detail', pk=product.id)
    else:
        form = ReviewForm()

    return render(request, 'reviews/add_review.html', {'form': form, 'product': product})

@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    
    # Check if the logged-in user is the one who created the review
    if review.user == request.user:
        review.delete()  # Delete the review
        return redirect('product-detail', pk=review.product.id)  # Redirect to the product detail page
    else:
        return redirect('product-detail', pk=review.product.id)  # Optional
import stripe
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Payment
from django.http import JsonResponse
from cart.models import CartItem
from decimal import Decimal
from django.core.mail import send_mail
from django.template.loader import render_to_string
from orders.models import Order, OrderItem 


stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required
def checkout(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total = sum(item.product.price * item.quantity for item in cart_items)

    intent = stripe.PaymentIntent.create(
        amount=int(total * Decimal('100')),
        currency='usd',
    )

    return render(request, "payments/checkout.html", {
        'client_secret': intent.client_secret,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
        'total': total
    })

@login_required
def payment_success(request):
    cart_items = CartItem.objects.filter(user=request.user)

    if not cart_items.exists():
        return redirect("cart")  # If cart is empty, redirect to cart page.

    # Create the order
    order = Order.objects.create(
        user=request.user,
        total_price=sum(item.product.price * item.quantity for item in cart_items),
        status='completed',  # Mark order as completed
    )

    # Create order items for each product in the cart
    for cart_item in cart_items:
        product = cart_item.product
        OrderItem.objects.create(
            order=order,
            product=product,
            quantity=cart_item.quantity,
            price=product.price * cart_item.quantity  # Store total price for the product
        )

    # Prepare email content
    subject = "ToolHub - Payment Confirmation"
    message = render_to_string("payments/email_receipt.html", {
        'user': request.user,
        'cart_items': cart_items,
        'order': order
    })
    recipient = request.user.email

    # Send email
    send_mail(subject, message, 'rand.jelo1@gmail.com', [recipient])

    # Clear the cart after sending the email
    cart_items.delete()

    return render(request, "payments/payment_success.html", {'order': order})

def payment_failed(request):
    return render(request, "payments/payment_failed.html")

@login_required
def create_payment_intent(request):
    cart_items = CartItem.objects.filter(user=request.user)

    if not cart_items.exists():
        return JsonResponse({'error': 'Your cart is empty.'}, status=400)

    total = sum(item.product.price * item.quantity for item in cart_items)
    total_cents = int(total * Decimal('100'))

    try:
        intent = stripe.PaymentIntent.create(
            amount=total_cents,
            currency='usd',
        )
        return JsonResponse({'clientSecret': intent.client_secret})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
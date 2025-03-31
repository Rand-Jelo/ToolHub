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
from django.utils.html import strip_tags


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
        return redirect("cart")

    total = sum(item.product.price * item.quantity for item in cart_items)

    order = Order.objects.create(
        user=request.user,
        total_price=total,
        status='completed',
    )

    for cart_item in cart_items:
        OrderItem.objects.create(
            order=order,
            product=cart_item.product,
            quantity=cart_item.quantity,
            price=cart_item.product.price * cart_item.quantity
        )

    context = {
        'user': request.user,
        'cart_items': cart_items,
        'order': order,
        'total': total,  # This is what was missing
    }

    subject = "ToolHub - Payment Confirmation"
    message = render_to_string("payments/email_receipt.html", context)
    plain_message = strip_tags(message)  # Create plain text version

    
    send_mail(
        subject,
        plain_message,
        'rand.jelo1@gmail.com',
        [request.user.email],
        html_message=message
    )

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
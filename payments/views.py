import stripe
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Payment

stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required
def checkout(request):
    amount = 5000  # $50.00 in cents for testing
    try:
        intent = stripe.PaymentIntent.create(
            amount=amount,
            currency='usd',
            metadata={'integration_check': 'accept_a_payment'},
        )
        return render(request, "payments/checkout.html", {
            'client_secret': intent.client_secret,
            'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY
        })
    except Exception as e:
        return render(request, "payments/payment_failed.html", {'error': str(e)})

def payment_success(request):
    return render(request, "payments/payment_success.html")

def payment_failed(request):
    return render(request, "payments/payment_failed.html")
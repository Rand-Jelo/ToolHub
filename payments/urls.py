from django.urls import path
from .views import checkout, payment_success, payment_failed, create_payment_intent

urlpatterns = [
    path('checkout/', checkout, name='checkout'),
    path('success/', payment_success, name='payment-success'),
    path('failed/', payment_failed, name='payment-failed'),
    path('create-payment-intent/', create_payment_intent, name='create-payment-intent'),
]
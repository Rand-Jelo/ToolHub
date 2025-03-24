from django.urls import path
from .views import checkout, payment_success, payment_failed

urlpatterns = [
    path('checkout/', checkout, name='checkout'),
    path('success/', payment_success, name='payment-success'),
    path('failed/', payment_failed, name='payment-failed'),
]
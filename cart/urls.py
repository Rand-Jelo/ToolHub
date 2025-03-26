from django.urls import path
from .views import view_cart, add_to_cart, remove_from_cart, update_cart_item

urlpatterns = [
    path('', view_cart, name='view-cart'),
    path('add/<int:product_id>/', add_to_cart, name='add-to-cart'),
    path('remove/<int:product_id>/', remove_from_cart, name='remove-from-cart'),
    path('update/<int:product_id>/', update_cart_item, name='update-cart-item'),
]
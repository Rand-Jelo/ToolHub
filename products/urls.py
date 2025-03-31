from django.urls import path
from .views import product_list, product_detail, delete_review

urlpatterns = [
    path('', product_list, name='product-list'),
    path('<int:pk>/', product_detail, name='product-detail'),
    path('review/delete/<int:review_id>/', delete_review, name='delete-review'),
]
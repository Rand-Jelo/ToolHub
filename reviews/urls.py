from django.urls import path
from .views import add_review, delete_review

urlpatterns = [
    path('add/<int:product_id>/', add_review, name='add-review'),
    path('delete/<int:review_id>/', delete_review, name='delete-review'),
]
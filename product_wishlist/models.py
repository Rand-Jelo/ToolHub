from django.db import models
from django.conf import settings
from products.models import Product

class Wishlist(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(Product, related_name='wishlists', blank=True)

    def __str__(self):
        return f"Wishlist of {self.user.username}"
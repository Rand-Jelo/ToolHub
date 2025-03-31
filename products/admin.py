from django.contrib import admin
from .models import Product, Tag

class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Tag, TagAdmin)
admin.site.register(Product)
import django_filters
from .models import Product, Tag

class ProductFilter(django_filters.FilterSet):
    # Add filters for the fields you want to filter by
    tag = django_filters.ModelChoiceFilter(queryset=Tag.objects.all(), empty_label="All Tags")
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte', label="Min Price")
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte', label="Max Price")

    class Meta:
        model = Product
        fields = ['tag', 'min_price', 'max_price']
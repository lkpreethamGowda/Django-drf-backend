
import django_filters
from .models import Product

class ProductFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name="pricing", lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name="pricing", lookup_expr='lte')
    product_name = django_filters.CharFilter(field_name="product_name", lookup_expr='icontains')
    label = django_filters.CharFilter(field_name="label")
    type = django_filters.CharFilter(field_name="type")

    class Meta:
        model = Product
        fields = ['product_name', 'label', 'type', 'min_price', 'max_price']

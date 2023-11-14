import django_filters
from django.db.models import Q
from django.db.models.functions import ExtractYear
from trendyol.models import Product, Tags


class ProductFilter(django_filters.FilterSet):
    search_name = django_filters.CharFilter(label='Search w name', method='filter_name')
    search_top_price = django_filters.CharFilter(label='Search w price', method='filter_by_price')
    search_bottom_price = django_filters.CharFilter(label='Search w BPrice', method='filter_by_Bprice')


    def filter_name(self, queryset, name, value):
        if value:
            return queryset.filter(name__icontains=value)
        return queryset

    def filter_by_price(self, queryset, name, value):
        if value:
            return queryset.filter(
                Q(price__lte=value)
            )

    def filter_by_Bprice(self, queryset, name, value):
        if value:
            return queryset.filter(
                Q(price__gte=value)
            )

    class Meta:
        model = Product
        fields = ("search_name", 'search_top_price', 'search_bottom_price', )

from django.urls import path
from trendyol.views import CategoryListView, ShopListView

urlpatterns = [
    path("", CategoryListView.as_view(), name="categories"),
    path("shops/", ShopListView.as_view(), name="shops"),
]
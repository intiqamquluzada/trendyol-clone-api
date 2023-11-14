from django.urls import path
from trendyol.views import (CategoryListView, ShopListView,
                            BrandListView, CommentView,ProductView,
                            TagListView, ColorView, SizeView)

urlpatterns = [
    path("", CategoryListView.as_view(), name="categories"),
    path("shops/", ShopListView.as_view(), name="shops"),
    path("brands/", BrandListView.as_view(), name='brands'),
    path("comments/", CommentView.as_view(), name='comments'),
    path("products/", ProductView.as_view(), name='products'),
    path("tags/", TagListView.as_view(), name="tags"),
    path("colors/", ColorView.as_view(), name="colors"),
    path("sizes/", SizeView.as_view(), name="sizes"),
]
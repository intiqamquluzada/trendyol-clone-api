from django.urls import path
from trendyol.views import (CategoryListView, ShopListView,
                            BrandListView, CommentView,)

urlpatterns = [
    path("", CategoryListView.as_view(), name="categories"),
    path("shops/", ShopListView.as_view(), name="shops"),
    path("brands/", BrandListView.as_view(), name='brands'),
    path("comments/", CommentView.as_view(), name='comments/')
]
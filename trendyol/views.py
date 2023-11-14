from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, CreateAPIView
from django.http import JsonResponse
from rest_framework import filters
from rest_framework.permissions import AllowAny
from .filters import ProductFilter
from django_filters.rest_framework.backends import DjangoFilterBackend
from trendyol.models import (Category, Shop, Brand,
                             Comment, Product, Tags,
                             Colors, Sizes)
from trendyol.serializers import (CategorySerializer, ShopSerializer,
                                  BrandSerializer, CommentSerializer,
                                  ProductSerializer, TagSerializer,
                                  ColorSerializer, SizeSerializer)


class CategoryListView(ListAPIView):
    queryset = Category.objects.order_by("-created_at")
    serializer_class = CategorySerializer


class ShopListView(ListAPIView):
    queryset = Shop.objects.order_by("-created_at")
    serializer_class = ShopSerializer


class BrandListView(ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class CommentView(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [AllowAny]

class ProductView(ListAPIView):
    queryset = Product.objects.order_by("-created_at")
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = ProductFilter


class TagListView(ListAPIView):
    queryset = Tags.objects.all()
    serializer_class = TagSerializer

class ColorView(ListAPIView):
    queryset = Colors.objects.order_by("name")
    serializer_class = ColorSerializer

class SizeView(ListAPIView):
    queryset = Sizes.objects.all()
    serializer_class = SizeSerializer

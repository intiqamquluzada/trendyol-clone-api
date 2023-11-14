from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, CreateAPIView
from django.http import JsonResponse
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
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



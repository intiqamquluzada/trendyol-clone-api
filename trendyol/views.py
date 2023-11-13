from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, CreateAPIView
from django.http import JsonResponse
from rest_framework.views import APIView
from trendyol.models import Category, Shop
from trendyol.serializers import (CategorySerializer, ShopSerializer)


class CategoryListView(ListAPIView):
    queryset = Category.objects.order_by("-created_at")
    serializer_class = CategorySerializer


class ShopListView(ListAPIView):
    queryset = Shop.objects.order_by("-created_at")
    serializer_class = ShopSerializer

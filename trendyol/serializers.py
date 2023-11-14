from rest_framework import serializers
from trendyol.models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("name", "parent", "created_at", "updated_at")


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = "__all__"


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sizes
        fields = "__all__"


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colors
        fields = "__all__"

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = "__all__"

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"





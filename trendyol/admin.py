from django.contrib import admin
from trendyol.models import (Category, Shop, Sizes, Colors, Product, Tags,
                             Features, Comment, ProductImages, Brand)


class ProductImageInlines(admin.StackedInline):
    model = ProductImages
    extra = 1


class ProductFeaturesInline(admin.StackedInline):
    model = Features
    extra = 1




class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInlines, ProductFeaturesInline]


admin.site.register(Category)
admin.site.register(Shop)
admin.site.register(Tags)
admin.site.register(Sizes)
admin.site.register(Colors)
admin.site.register(Product, ProductAdmin)
admin.site.register(Comment)
admin.site.register(Brand)
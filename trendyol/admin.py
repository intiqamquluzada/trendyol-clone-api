from django.contrib import admin
from trendyol.models import (Category, Shop, Sizes, Colors, Product, Tags,
                             Features, Comment)


admin.site.register(Category)
admin.site.register(Shop)
admin.site.register(Tags)
admin.site.register(Sizes)
admin.site.register(Colors)
admin.site.register(Product)
admin.site.register(Features)
admin.site.register(Comment)


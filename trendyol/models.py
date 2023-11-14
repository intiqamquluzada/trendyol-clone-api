from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from services.mixin import DateMixin, SlugMixin
from services.generator import unique_slug_generator, custom_slugify
from services.uploader import Uploader
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(MPTTModel):
    name = models.CharField(max_length=255, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.parent:
            return f"{self.parent}->{self.name}"
        return self.name

    class Meta:
        ordering = ("name",)
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Shop(DateMixin, SlugMixin):
    name = models.CharField(max_length=255, verbose_name="Shop name")
    logo = models.ImageField(upload_to=Uploader.upload_photo_for_shop, verbose_name="Shop logo")
    status = models.CharField(max_length=255, verbose_name="Shop's main feature")
    location = models.CharField(max_length=255, verbose_name="Location of shop")
    trendyol_adventure_time = models.CharField(max_length=255, verbose_name="Time length in Trendyol")
    have_receipt = models.BooleanField(default=True)
    answer_time = models.CharField(max_length=255, verbose_name="Average reply time")
    cargo_time = models.CharField(max_length=255, verbose_name="Average to cargo time")
    rating = models.FloatField(verbose_name="Rating value", editable=False, default=0)

    followers = models.ManyToManyField(User, verbose_name="Followers of shop", null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("rating", "-created_at")
        verbose_name = "Shop"
        verbose_name_plural = "Shops"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slug_generator(self, custom_slugify(f"{self.name}"))
        super(Shop, self).save(*args, **kwargs)


class Sizes(DateMixin, SlugMixin):
    name = models.CharField(max_length=255, verbose_name="Sizes of clothes")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Size"
        verbose_name_plural = "Sizes"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slug_generator(self, custom_slugify(f"{self.name}"))
        super(Sizes, self).save(*args, **kwargs)


class Colors(DateMixin, SlugMixin):
    name = models.CharField(max_length=255, verbose_name="Color")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Color"
        verbose_name_plural = "Colors"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slug_generator(self, custom_slugify(f"{self.name}"))
        super(Colors, self).save(*args, **kwargs)


class Tags(DateMixin, SlugMixin):
    name = models.CharField(max_length=255, verbose_name="Tag")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slug_generator(self, custom_slugify(f"{self.name}"))
        super(Tags, self).save(*args, **kwargs)

class Brand(DateMixin, SlugMixin):
    name = models.CharField(max_length=255, verbose_name="Brand")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("-created_at", )
        verbose_name = "Brand"
        verbose_name_plural = "Brands"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slug_generator(self, custom_slugify(f"{self.name}"))
        super(Brand, self).save(*args, **kwargs)


class Product(DateMixin, SlugMixin):
    categories = models.ManyToManyField(Category, verbose_name="Category")
    name = models.CharField(max_length=255, verbose_name="Name of product")
    rating = models.FloatField(verbose_name="Rating of product", editable=False, default=0)
    price = models.FloatField(verbose_name="Price of product")
    discount_price = models.FloatField(verbose_name="Discount price (if has)", null=True, blank=True)
    shop = models.ForeignKey(Shop, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Shop")
    size = models.ManyToManyField(Sizes, verbose_name="Sizes of product")
    color = models.ManyToManyField(Colors, verbose_name="Colors of product")
    tag = models.ForeignKey(Tags, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Tag of product")
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Brand")

    for_aze = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slug_generator(self, custom_slugify(f"{self.name}"))
        super(Product, self).save(*args, **kwargs)


class Features(DateMixin, SlugMixin):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Product")
    name = models.CharField(max_length=255, verbose_name="Key")
    value = models.CharField(max_length=255, verbose_name="Value")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Feature"
        verbose_name_plural = "Features of products"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slug_generator(self, custom_slugify(f"{self.name}"))
        super(Features, self).save(*args, **kwargs)




class Comment(DateMixin):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="User")
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Product")
    text = models.TextField(verbose_name="Text")

    def __str__(self):
        return self.product

    class Meta:
        ordering = ("-created_at", )
        verbose_name = "Comment"
        verbose_name_plural = "Comments"




class ProductImages(DateMixin):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Product")
    image = models.ImageField(upload_to=Uploader.upload_photo_for_product, verbose_name="Photo for product")

    def __str__(self):
        return self.product.name

    class Meta:
        ordering = ("-created_at", )
        verbose_name = "Product Image"
        verbose_name_plural = "Product Images"




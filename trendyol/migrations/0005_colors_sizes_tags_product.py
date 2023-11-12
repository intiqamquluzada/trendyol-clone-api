# Generated by Django 4.2.7 on 2023-11-12 23:03

from django.db import migrations, models
import django.db.models.deletion
import services.uploader


class Migration(migrations.Migration):

    dependencies = [
        ('trendyol', '0004_shop'),
    ]

    operations = [
        migrations.CreateModel(
            name='Colors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(blank=True, editable=False, max_length=255, unique=True)),
                ('name', models.CharField(max_length=255, verbose_name='Color')),
                ('photo', models.ImageField(upload_to=services.uploader.Uploader.upload_photo_for_product, verbose_name='Product photo')),
            ],
            options={
                'verbose_name': 'Color',
                'verbose_name_plural': 'Colors',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='Sizes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(blank=True, editable=False, max_length=255, unique=True)),
                ('name', models.CharField(max_length=255, verbose_name='Sizes of clothes')),
            ],
            options={
                'verbose_name': 'Size',
                'verbose_name_plural': 'Sizes',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(blank=True, editable=False, max_length=255, unique=True)),
                ('name', models.CharField(max_length=255, verbose_name='Tag')),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(blank=True, editable=False, max_length=255, unique=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name of product')),
                ('rating', models.FloatField(verbose_name='Rating of product')),
                ('price', models.FloatField(verbose_name='Price of product')),
                ('discount_price', models.FloatField(blank=True, null=True, verbose_name='Discount price (if has)')),
                ('for_aze', models.BooleanField(default=False)),
                ('categories', models.ManyToManyField(to='trendyol.category', verbose_name='Category')),
                ('color', models.ManyToManyField(to='trendyol.colors', verbose_name='Colors of product')),
                ('shop', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='trendyol.shop', verbose_name='Shop')),
                ('size', models.ManyToManyField(to='trendyol.sizes', verbose_name='Sizes of product')),
                ('tag', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='trendyol.tags', verbose_name='Tag of product')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'ordering': ('-created_at',),
            },
        ),
    ]

# Generated by Django 4.2.4 on 2024-02-22 17:12

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion
import utils.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Name')),
                ('slug', models.SlugField(blank=True, null=True, unique=True, verbose_name='Slug')),
                ('show_hide', models.BooleanField(default=True, verbose_name='Show/Hide')),
            ],
            options={
                'verbose_name': 'Brand',
                'verbose_name_plural': 'Brands',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True, verbose_name='Category')),
                ('slug', models.SlugField(blank=True, null=True, unique=True, verbose_name='Slug')),
                ('show_hide', models.BooleanField(default=True, verbose_name='Show/Hide')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Name')),
                ('slug', models.SlugField(blank=True, null=True, unique=True, verbose_name='Slug')),
                ('image', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, validators=[utils.validators.validate_extension], verbose_name='Image')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('discount', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Discount')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='Start Date')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='End Date')),
                ('status', models.BooleanField(default=True, verbose_name='Status')),
            ],
            options={
                'verbose_name': 'Deal',
                'verbose_name_plural': 'deals',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('slug', models.SlugField(blank=True, null=True, unique=True, verbose_name='Slug')),
                ('normal_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price')),
                ('sale_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Sale Price')),
                ('image', cloudinary.models.CloudinaryField(blank=True, max_length=255, validators=[utils.validators.validate_extension], verbose_name='Image')),
                ('stock', models.PositiveIntegerField(default=100, verbose_name='Stock')),
                ('warranty', models.IntegerField(blank=True, choices=[(1, '1 month'), (3, '3 months'), (6, '6 months'), (12, '1 year'), (24, '2 years'), (36, '3 years')], default='12', verbose_name='Warranty')),
                ('featured', models.BooleanField(default=False, verbose_name='Featured')),
                ('show_hide', models.BooleanField(default=True, verbose_name='Show/Hide')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('specifications', models.TextField(blank=True, null=True, verbose_name='Specifications')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.brand', verbose_name='Brand')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.category', verbose_name='Category')),
                ('deal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='products.deal', verbose_name='Deal')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'ordering': ['title'],
            },
        ),
    ]

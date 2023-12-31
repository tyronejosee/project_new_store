# Generated by Django 4.2.4 on 2023-10-16 19:24

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


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
                ('show_hide', models.BooleanField(default=True, verbose_name='Show/Hide')),
            ],
            options={
                'verbose_name_plural': 'Brands',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True, verbose_name='Category')),
                ('section', models.IntegerField(choices=[(1, 'pending'), (2, 'Electronic Deals'), (3, 'TVs & Home Theater'), (4, 'Cell Phones'), (5, 'Computers & Office'), (6, 'Kids Electronics'), (7, 'Headphones'), (8, 'Cameras'), (9, 'Speakers & Audio Systems'), (10, 'Tablets & E-Readers'), (11, 'Wearable Technology'), (12, 'Wi-Fi & Networking')], default='1')),
                ('show_hide', models.BooleanField(default=True, verbose_name='Show/Hide')),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('normal_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price')),
                ('image', models.ImageField(upload_to='products/', verbose_name='Image')),
                ('stock', models.PositiveIntegerField(blank=True, default=100, null=True, verbose_name='Stock')),
                ('warranty', models.IntegerField(blank=True, choices=[(1, '1 month'), (3, '3 months'), (6, '6 months'), (12, '1 year'), (24, '2 years'), (36, '3 years')], default='12', null=True)),
                ('discount_percentage', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('discount_end_date', models.DateField(blank=True, null=True)),
                ('featured', models.BooleanField(default=False, verbose_name='Featured')),
                ('show_hide', models.BooleanField(default=True, verbose_name='Show/Hide')),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Description')),
                ('specifications', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Specifications')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.brand', verbose_name='Brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category', verbose_name='Category')),
            ],
            options={
                'verbose_name_plural': 'Products',
                'ordering': ['-created_at', 'title'],
            },
        ),
    ]

# Generated by Django 4.2.4 on 2023-10-18 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='discount_end_date',
        ),
        migrations.RemoveField(
            model_name='product',
            name='discount_percentage',
        ),
    ]

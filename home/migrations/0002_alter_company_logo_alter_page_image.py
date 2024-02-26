# Generated by Django 4.2.4 on 2024-02-23 16:31

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='Logo'),
        ),
        migrations.AlterField(
            model_name='page',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='Logo'),
        ),
    ]

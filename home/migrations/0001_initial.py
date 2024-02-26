# Generated by Django 4.2.4 on 2024-02-22 17:12

import cloudinary.models
from django.db import migrations, models
import utils.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('logo', cloudinary.models.CloudinaryField(max_length=255, validators=[utils.validators.validate_extension], verbose_name='Logo')),
                ('copy', models.CharField(max_length=150, verbose_name='Copy')),
                ('description', models.TextField(verbose_name='Description')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('github', models.URLField(verbose_name='GitHub')),
                ('linkedin', models.URLField(verbose_name='LinkedIn')),
            ],
            options={
                'verbose_name': 'Company',
                'verbose_name_plural': 'Company',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(default='pending', max_length=50, verbose_name='Unique Key')),
                ('content', models.TextField(blank=True, verbose_name='Content')),
                ('image', cloudinary.models.CloudinaryField(max_length=255, validators=[utils.validators.validate_extension], verbose_name='Logo')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
            ],
            options={
                'verbose_name': 'Page',
                'verbose_name_plural': 'Pages',
                'ordering': ['key'],
            },
        ),
    ]

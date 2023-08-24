from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=15, unique=True)
    extention = models.CharField(max_length=2, unique=True)


    def __str__(self):
        return self.name


class User(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    username = models.CharField(max_length=50, unique=True)
    firt_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    tax_number = models.CharField(max_length=25, unique=True)
    email = models.CharField(max_length=25, unique=True)
    password = models.CharField(max_length=128)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    adress = models.CharField(max_length=75)
    city = models.CharField(max_length=50)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)


    def __str__(self):
        return self.username


    def save(self, *args, **kwargs):
        # Al guardar el objeto Usuario, asegúrate de que la contraseña se almacene como un hash
        self.password = make_password(self.password)
        super().save(*args, **kwargs)

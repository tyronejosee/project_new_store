""" Users Accounts Models """
import os
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save
#from PIL import Image

# Choices
VERIFICATION_OPTIONS=(
    ('unverified', 'unverified'),
    ('verified', 'verified'),
)

GENDER_CHOICES=(
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
)


def user_directory_path_profile(instance, filename):
    """
    Genera la ruta de almacenamiento de la imagen de perfil del usuario.
    
    :param instance: Instancia del perfil de usuario.
    :param filename: Nombre original del archivo.
    :return: Ruta de almacenamiento.
    """


    profile_picture_name = 'users/{0}/profile.jpg'.format(instance.user.username)
    full_path = os.path.join(settings.MEDIA_ROOT, profile_picture_name)

    if os.path.exists(full_path):
        os.remove(full_path)

    return profile_picture_name

# Definición de Modelos
class Country(models.Model):
    """Modelo tipo catálogo para los países"""
    name = models.CharField(max_length=15, unique=True)
    extention = models.CharField(max_length=2, unique=True)

    def __str__(self):
        return str(self.name)


class User(AbstractUser):
    """Modelo personalizado de usuario."""
    # Campos Adicionales
    adress = models.CharField(max_length=75)
    city = models.CharField(max_length=50)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    tax_number = models.CharField(max_length=25, unique=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'


class Profile(models.Model):
    """
    Modelo de perfil de usuario.
    """
    verified = models.CharField(max_length=10, choices=VERIFICATION_OPTIONS, default='unverified')
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    picture = models.ImageField(default='users/default_profile.png', upload_to=user_directory_path_profile)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username


# Funciones de Utilidad
def create_user_profile(sender, instance, created, **kwargs):
    """
    Crea un perfil de usuario al crear un nuevo usuario.
    """
    if created:
        Profile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
    """
    Guarda el perfil de usuario al guardar el usuario.
    """
    instance.profile.save()


# Conexiones de señales para crear y guardar perfiles
post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)

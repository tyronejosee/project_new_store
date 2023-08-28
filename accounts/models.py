from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
import os
from PIL import Image
from django.db.models.signals import post_save


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

def delete_file_safely(file_path):
    """
    Elimina un archivo de manera segura.
    
    :param file_path: Ruta del archivo a eliminar.
    """
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
    except Exception as e:
        print(f"An error occurred while deleting file: {file_path}")
        print(str(e))

def user_directory_path_profile(instance, filename):
    """
    Genera la ruta de almacenamiento de la imagen de perfil del usuario.
    
    :param instance: Instancia del perfil de usuario.
    :param filename: Nombre original del archivo.
    :return: Ruta de almacenamiento.
    """
    profile_picture_name = f'users/{instance.user.username}/profile.jpg'
    full_path = os.path.join(settings.MEDIA_ROOT, profile_picture_name)

    delete_file_safely(full_path)

    return profile_picture_name

# Definición de Modelos
class Country(models.Model):
    name = models.CharField(max_length=15, unique=True)
    extention = models.CharField(max_length=2, unique=True)

    def __str__(self):
        """
        Representación del nombre del país.
        """
        return str(self.name)


class User(AbstractUser):
    """
    Modelo personalizado de usuario.
    """


class Profile(models.Model):
    """
    Modelo de perfil de usuario.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    picture = models.ImageField(default='users/default_profile.png', upload_to=user_directory_path_profile)
    verified = models.CharField(max_length=10, choices=VERIFICATION_OPTIONS, default='unverified')
    date_created = models.DateField(auto_now_add=True)
    location = models.CharField(max_length=50, null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    adress = models.CharField(max_length=75)
    city = models.CharField(max_length=50)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    tax_number = models.CharField(max_length=25, unique=True)

    def __str__(self):
        """
        Representación en cadena del perfil de usuario.
        """
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

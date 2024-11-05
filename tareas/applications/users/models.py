from django.db import models
#
from model_utils.models import TimeStampedModel
#
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
#
from .managers import UserManager

# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):
    full_name = models.CharField('Nombre Completo', max_length=150)
    email = models.EmailField('Correo Electgronico', max_length=254, unique=True)
    address = models.CharField('Direccion', max_length=50, blank=True, null=True)
    date_birth = models.DateField('Fecha Nacimiento', blank=True, null=True)    
    phone = models.CharField('Telefono', max_length=20, blank=True, null=True)
    photo = models.ImageField('Foto', upload_to='avatar', blank=True, null=True)
    #
    is_active = models.BooleanField('Activo', default=False)
    is_superuser = models.BooleanField('SuperUsuario', default=False)
    is_staff = models.BooleanField('Staff', default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    objects = UserManager()

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
    

    def get_full_name(self):
        return self.full_name
    

    def get_email(self):
        return self.email
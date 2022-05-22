from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UserManager(BaseUserManager):
    '''Manager para perfiles de usuarios, para espesificar funciones
    que sirven para manipular lo que tenemos dentro de nuestros objetos UserProfiles'''
    def create_user(self, email, name, password=None):
        '''Crear nuevo perfil de usuario '''
        if not email:
            raise ValueError('Usuario debe tener un Email')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    ''' Modelo base de datos para usuarios en el sistema'''
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    # cuando el usuario se crea esta activo
    is_active = models.BooleanField(default=True)
    # si son miembros del equipo
    is_staff = models.BooleanField(default=False)
    # espesificamos el modo manager para nuestros objetos
    objects = UserManager()
    # Campo de login que el usuario va a espesificar
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        '''Obtener nombre completo'''
        return self.name
    
    def get_short_name(self):
        '''Obtener nombre corto'''
        return self.name

    def __str__(self):
        '''Retornar cadena Representando nuestro usuario'''
        return self.email

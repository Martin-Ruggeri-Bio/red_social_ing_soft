from django.contrib import admin
from profiles_api import models

# le estamos dando acseso al administrador para que pueda editar y crear modelos de UserProfile
admin.site.register(models.UserProfile)

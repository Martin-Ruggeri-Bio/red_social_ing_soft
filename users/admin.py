from django.contrib import admin
from users import models

# le estamos dando acseso al administrador para que pueda editar y crear modelos de UserProfile
admin.site.register(models.User)

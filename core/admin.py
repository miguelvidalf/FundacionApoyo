from django.contrib import admin
from .models import Categoria, Post, Vehiculo, PerfilUsuario, Paciente, Insumo

# Register your models here.

admin.site.register(Categoria)
admin.site.register(Vehiculo)
admin.site.register(PerfilUsuario)
admin.site.register(Paciente)
admin.site.register(Insumo)
admin.site.register(Post)



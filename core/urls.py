from django.urls import path
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views
from .views import administrar_pacientes, home, administrar_productos, tienda, ficha, administrar_insumos
from .views import iniciar_sesion, registrar_usuario, cerrar_sesion
from .views import perfil_usuario, iniciar_pago, pago_exitoso
from .views import  index
from .views_poblar_bd import poblar_bd
from .views import administrar_pacientes,paciente,ficha_paciente, administrar_insumos

urlpatterns = [
    path('', home, name="home"),
    path('index', index, name="index"),
    path('poblar_bd', poblar_bd, name="poblar_bd"),
    path('administrar_productos/<action>/<id>', administrar_productos, name="administrar_productos"),
    path('tienda', tienda, name="tienda"),
    path('ficha/<id>', ficha, name="ficha"),
    path('iniciar_sesion/', iniciar_sesion, name="iniciar_sesion"),
    path('cerrar_sesion/', cerrar_sesion, name='cerrar_sesion'),
    path('registrar_usuario/', registrar_usuario, name="registrar_usuario"),
    path('password_cambiada/', TemplateView.as_view(template_name='core/password_cambiada.html'), name='password_cambiada'),
    path('cambiar_password/', auth_views.PasswordChangeView.as_view(template_name='core/cambiar_password.html', success_url='/password_cambiada'), name='cambiar_password'),
    path('perfil_usuario/', perfil_usuario, name="perfil_usuario"),
    path('iniciar_pago/', iniciar_pago, name="iniciar_pago"),
    path('pago_exitoso/', pago_exitoso, name="pago_exitoso"),
    path('administrar_pacientes/<action>/<id>', administrar_pacientes, name="administrar_pacientes"),
    path('pacientes/', paciente, name="pacientes"),
    path('ficha_paciente/<id>',ficha_paciente, name="ficha_paciente"),
    path('administrar_insumos/<action>/<id>', administrar_insumos, name="administrar_insumos"),
]
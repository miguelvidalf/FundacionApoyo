from pyexpat import model
from django import forms
from django.forms import ModelForm, fields, Form
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Vehiculo, PerfilUsuario, Paciente, Insumo, Post

class VehiculoForm(ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['patente', 'marca', 'modelo', 'imagen', 'precio', 'categoria']

class IniciarSesionForm(Form):
    username = forms.CharField(widget=forms.TextInput(), label="Correo")
    password = forms.CharField(widget=forms.PasswordInput(), label="Contraseña")
    class Meta:
        fields = ['username', 'password']

class RegistrarUsuarioForm(UserCreationForm):
    rut = forms.CharField(max_length=80, required=True, label="Rut")
    direccion = forms.CharField(max_length=80, required=True, label="Dirección")
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'rut', 'direccion']

class PerfilUsuarioForm(Form):
    first_name = forms.CharField(max_length=150, required=True, label="Nombres")
    last_name = forms.CharField(max_length=150, required=True, label="Apellidos")
    email = forms.CharField(max_length=254, required=True, label="Correo")
    rut = forms.CharField(max_length=80, required=False, label="Rut")
    direccion = forms.CharField(max_length=80, required=False, label="Dirección")

    class Meta:
        fields = '__all__'
        
class PacienteForm(ModelForm):
    class Meta:
        model = Paciente
        fields = ['habitacion','rut','nombres','apellidos','direccion','ciudad','fnacimiento','edad','sexo','telefono','fingreso','fsalida','fresponsable','tcontacto','correo','antmedicos','alergias','enfermedades','medicamentos','cuidados','foto']
        def __init__(self, *args, **kwargs):
            super(PacienteForm,self).__init__(*args, **kwargs)
            self.fields['fnacimiento'].widget = forms.DateInput(attrs={ 'type': 'date'})
            self.fields['fingreso'].widget = forms.DateInput(attrs={ 'type': 'date'})
            self.fields['fsalida'].widget = forms.DateInput(attrs={ 'type': 'date'})
            
class InsumoForm(ModelForm):
    class Meta:
        model = Insumo
        fields = ['codigo','nombrein','punitario','cantidad','fcompra','estado','proveedor','descripcion']
        def __init__(self, *args, **kwargs):
            super(InsumoForm,self).__init__(*args, **kwargs)
            self.fields['fcompra'].widget = forms.DateInput(attrs={ 'type': 'date'})
            
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['residente','titulo','encargado','fecha','hora','anotacion']
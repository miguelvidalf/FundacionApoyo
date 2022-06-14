from operator import mod
from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name="Id de categoría")
    nombreCategoria = models.CharField(max_length=80, blank=False, null=False, verbose_name="Nombre de la categoría")

    def __str__(self):
        return f"{self.idCategoria} - {self.nombreCategoria}"

class Vehiculo(models.Model):
    patente = models.CharField(max_length=6, primary_key=True, verbose_name="Patente")
    marca = models.CharField(max_length=80, blank=False, null=False, verbose_name="Marca vehículo")
    modelo = models.CharField(max_length=80, null=True, blank=True, verbose_name="Modelo")
    imagen = models.ImageField(upload_to="images/", default="sinfoto.jpg", null=False, blank=False, verbose_name="Imagen")
    precio = models.DecimalField(max_digits=35, decimal_places=2, null=False, blank=False, verbose_name="Precio")
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    

    def __str__(self):
        return f"{self.patente} - {self.marca}, {self.modelo}"

class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rut = models.CharField(max_length=80, blank=True, null=True, verbose_name="Rut")
    direccion = models.CharField(max_length=80, blank=True, null=True, verbose_name="Dirección")

    def __str__(self):
        return f"{self.user.username} - {self.user.first_name} {self.user.last_name} ({self.user.email})"
    
class Paciente(models.Model):
    rut = models.CharField(max_length=12, primary_key=True, verbose_name="Rut")
    nombres = models.CharField(max_length=80, blank=False, null=False, verbose_name="Nombres")
    apellidos = models.CharField(max_length=80, blank=False, null=False, verbose_name="Apellidos")
    direccion = models.CharField(max_length=80, blank=False, null=False, verbose_name="Direccion")
    ciudad = models.CharField(max_length=80, blank=False, null=False, verbose_name="Ciudad")
    fnacimiento = models.DateField(blank=False, null=False, verbose_name="Fecha de nacimiento")
    edad = models.IntegerField(null=False, blank=False, verbose_name="Edad")
    sexo = models.CharField(max_length=1, blank=False, null=False, verbose_name="sexo")
    telefono = models.CharField(max_length=14, verbose_name="Teléfono")
    fingreso = models.DateField(blank=False, null=False, verbose_name="Fecha de ingreso")
    fsalida = models.DateField(blank=True, null=True, verbose_name="Fecha de salida")
    fresponsable = models.CharField(max_length=80, blank=False, null=False, verbose_name="Famliar responsable")
    tcontacto = models.CharField(max_length=14, verbose_name="Teléfono contacto")
    correo = models.CharField(max_length=70, null=False, blank=False, verbose_name="Correo")
    antmedicos = models.CharField(max_length=800, blank=True, null=True, verbose_name="Antecedentes Médicos")
    alergias = models.CharField(max_length=800, blank=True, null=True, verbose_name="Alergias")
    enfermedades = models.CharField(max_length=800, blank=True, null=True, verbose_name="Enfermedades Pre-existentes")
    medicamentos = models.CharField(max_length=800, blank=True, null=True, verbose_name="medicamentos uso diario")
    habitacion = models.CharField(max_length=3, blank=False, null=False, verbose_name="Nro. de Habitación")
    cuidados = models.CharField(max_length=30, blank=False, null=False, verbose_name="Nivel de cuidado")
    foto = models.ImageField(upload_to="images/", default="sinfoto.jpg", null=False, blank=False, verbose_name="foto")
    def __str__(self):
        return f"{self.nombres} - {self.apellidos}, {self.rut}"
    
class Insumo(models.Model):
    codigo = models.CharField(max_length=12, primary_key=True, verbose_name="Código")
    nombrein = models.CharField(max_length=80, blank=False, null=False, verbose_name="Nombre")
    descripcion = models.TextField(max_length=80, verbose_name="Descripción")
    punitario = models.CharField(max_length=80, blank=False, null=False, verbose_name="Precio Unitario")
    cantidad = models.CharField(max_length=10, null=False, blank=False, verbose_name="Cantidad")
    fcompra = models.DateField(blank=False, null=False, verbose_name="Fecha de Compra")
    estado = models.CharField(max_length=30, blank=False, null=False, verbose_name="Estado")
    proveedor = models.CharField(max_length=80, blank=True, null=False, verbose_name="Proveedor")
    def __str__(self):
        return f"{self.codigo} - {self.nombrein}, {self.cantidad}, {self.estado}"
    
class Post(models.Model):
    residente = models.ForeignKey(Paciente, on_delete= models.CASCADE)
    titulo = models.CharField(max_length=60, null=False, blank=False, verbose_name="Titulo")
    encargado = models.CharField(max_length=60, null=False, blank=False, verbose_name="Encargado")
    fecha = models.DateField(blank=False, null=False,verbose_name="Fecha")
    hora = models.CharField(max_length=8, null=False, blank=False, verbose_name="Hora")
    anotacion = models.TextField(verbose_name="Anotacion")
    def __str__(self):
        return f"{self.residente} - {self.titulo}, {self.encargado},{self.fecha}"
    
    
    
    
    
    
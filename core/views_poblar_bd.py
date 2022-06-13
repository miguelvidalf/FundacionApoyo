from django.shortcuts import redirect
from django.contrib.auth.models import User
from .models import Vehiculo, Categoria, PerfilUsuario, Paciente
from .views import administrar_productos, administrar_pacientes

def poblar_bd(request):
    try:
        print("Verificar si existe usuario cliente.")
        if User.objects.filter(username="usuario_cliente").exists():
            print("Intentando eliminar usuario cliente.")
            User.objects.get(username="usuario_cliente").delete()
            print("Usuario cliente eliminado.")
        print("Iniciando creación de usuario cliente.")
        user = User.objects.create_user(username="usuario_cliente", password='Duoc@123')
        user.first_name = "Chris"
        user.last_name = "Evans (Cliente)"
        user.email = "cevans@marvel.com"
        user.is_superuser = False
        user.is_staff = False
        PerfilUsuario.objects.create(user=user, rut="11.111.111-K", direccion="Burbank (Estados Unidos)")
        user.save()
        print("Usuario cliente fue creado correctamente.")
    except Exception as err:
        print(f"Error al crear usuario cliente: {err}")
    try:
        print("Verificar si existe usuario staff.")
        if User.objects.filter(username="usuario_staff").exists():
            print("Intentando eliminar usuario staff.")
            User.objects.get(username="usuario_staff").delete()
            print("Usuario staff eliminado.")
        print("Iniciando creación de usuario staff.")
        user = User.objects.create_user(username="usuario_staff", password='Duoc@123')
        user.first_name = "Pepper"
        user.last_name = "Potts (Staff)"
        user.email = "ppotts@tiendastark.com"
        user.is_superuser = True
        user.is_staff = True
        PerfilUsuario.objects.create(user=user, rut="22.222.222-K", direccion="Burbank (Estados Unidos)")
        user.save()
        print("Usuario staff fue creado correctamente.")
    except Exception as err:
        print(f"Error al crear usuario staff: {err}")
    try:
        Vehiculo.objects.all().delete()
        print("Tabla Vehiculo fue truncada.")
        Categoria.objects.all().delete()
        print("Tabla Categoria fue truncada.")
        print("Iniciar poblamiento de tabla Categoria.")
        Categoria.objects.create(idCategoria=1, nombreCategoria="Camioneta")
        Categoria.objects.create(idCategoria=2, nombreCategoria="Automóvil")
        Categoria.objects.create(idCategoria=3, nombreCategoria="Motocicleta")
        print("Tabla Categoria fue poblada.")
    except Exception as err:
        print(f"Error al poblar tabla Categoria: {err}")
    try:
        print("Iniciar poblamiento de tabla Vehiculo.")
        Vehiculo.objects.create(patente="ALAN67", marca='Volvo', modelo="Volvo Station Wagon", imagen="images/volvosw.jpg", precio=700000000, categoria=Categoria.objects.get(idCategoria=2))
        Vehiculo.objects.create(patente="BILL88", marca='Saleen', modelo="S7", imagen="images/saleen.jpg", precio=600000000, categoria=Categoria.objects.get(idCategoria=2))
        Vehiculo.objects.create(patente="ELVI54", marca='Shelby', modelo="Cobra de 1967", imagen="images/cobra.jpg", precio=600000000, categoria=Categoria.objects.get(idCategoria=2))
        Vehiculo.objects.create(patente="FEDE84", marca='Mercedes-Benz', modelo="Pagoda de 1972", imagen="images/pagoda.jpg", precio=800000000, categoria=Categoria.objects.get(idCategoria=2))
        Vehiculo.objects.create(patente="JEFF46", marca='Ford', modelo="Wolf WR1 Ford Race Car", imagen="images/wolf.jpg", precio=700000000, categoria=Categoria.objects.get(idCategoria=2))
        Vehiculo.objects.create(patente="JOHN80", marca='Ford', modelo="Flathead Roadster de 1932", imagen="images/flathead.jpg", precio=600000000, categoria=Categoria.objects.get(idCategoria=2))
        Vehiculo.objects.create(patente="PAUL62", marca='Rolls-Royce', modelo="Phantom", imagen="images/phantom.jpg", precio=500000000, categoria=Categoria.objects.get(idCategoria=2))
        Vehiculo.objects.create(patente="SCAR47", marca='Mustang', modelo="Mustang de 1970", imagen="images/mustang.jpg", precio=400000000, categoria=Categoria.objects.get(idCategoria=2))
        Vehiculo.objects.create(patente="TIRO98", marca='Mercedes-Benz', modelo="Iron Bike de 1998", imagen="images/motoiron.jpg", precio=300000000, categoria=Categoria.objects.get(idCategoria=3))
        Vehiculo.objects.create(patente="UVAM20", marca='Silver Plus', modelo="Silver de 2000", imagen="images/silver.jpg", precio=200000000, categoria=Categoria.objects.get(idCategoria=3))
        print("Tabla Vehiculo fue poblada.")
    except Exception as err:
        print(f"Error al poblar vehículos: {err}")
    
    #Poblar pacientes
    #try:
    #    Paciente.objects.all().delete()
     #   print("Tabla paciente fue truncada.")
    #except Exception as err:
     #   print(f"Error al borrar pacientes: {err}")
    
    #try:
     #   Paciente.objects.create(rut="18737496-0", nombres="Miguel Alejandro", apellidos="Vidal Fernandez", direccion="san pio #3122", ciudad="Santiago", fnacimiento="23/02/1994")
    
    #except Exception as err:
     #   print(f"Error al poblar vehículos: {err}")
         
    
    
    
    #return redirect(administrar_productos, action='ins', id = '-1')

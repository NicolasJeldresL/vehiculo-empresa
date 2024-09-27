from .models import Vehiculo, Chofer, RegistroContable


def crear_vehiculo(marca, modelo, año):
    return Vehiculo.objects.create(marca=marca, modelo=modelo, año=año)


def crear_chofer(nombre, apellido, licencia_conducir):
    return Chofer.objects.create(nombre=nombre, apellido=apellido, licencia_conducir=licencia_conducir)


def crear_registro_contable(vehiculo_id, fecha_registro, monto, descripcion):
    vehiculo = Vehiculo.objects.get(id=vehiculo_id)
    return RegistroContable.objects.create(vehiculo=vehiculo, fecha_registro=fecha_registro, monto=monto, descripcion=descripcion)


def deshabilitar_chofer(chofer_id):
    chofer = Chofer.objects.get(id=chofer_id)
    chofer.habilitado = False
    chofer.save()

def habilitar_chofer(chofer_id):
    chofer = Chofer.objects.get(id=chofer_id)
    chofer.habilitado = True
    chofer.save()


def deshabilitar_vehiculo(vehiculo_id):
    vehiculo = Vehiculo.objects.get(id=vehiculo_id)
    vehiculo.disponible = False
    vehiculo.save()

def habilitar_vehiculo(vehiculo_id):
    vehiculo = Vehiculo.objects.get(id=vehiculo_id)
    vehiculo.disponible = True
    vehiculo.save()

def asignar_chofer_a_vehiculo(chofer_id, vehiculo_id):
    vehiculo = Vehiculo.objects.get(id=vehiculo_id)
    chofer = Chofer.objects.get(id=chofer_id)
    vehiculo.chofer = chofer
    vehiculo.save()

def obtener_vehiculo(vehiculo_id):
    return Vehiculo.objects.get(id=vehiculo_id)

def obtener_chofer(chofer_id):
    return Chofer.objects.get(id=chofer_id)


def imprimir_datos_vehiculos():
    vehiculos = Vehiculo.objects.all()
    for vehiculo in vehiculos:
        print(f'ID: {vehiculo.id}, Marca: {vehiculo.marca}, Modelo: {vehiculo.modelo}, Año: {vehiculo.año}, Disponible: {vehiculo.disponible}')

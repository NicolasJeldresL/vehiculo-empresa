from django.db import models

class Vehiculo(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    año = models.IntegerField()
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.marca} {self.modelo} ({self.año})'

class Chofer(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    licencia_conducir = models.CharField(max_length=20)
    habilitado = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class RegistroContable(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    fecha_registro = models.DateField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return f'Registro {self.id} - {self.vehiculo}'

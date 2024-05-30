from django.db import models

class facultades(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    ubicacion = models.CharField(max_length=15)
    nro_telefono = models.CharField(max_length=15, null=True, blank=True)
    id_decano = models.CharField(max_length=15, null=True, blank=True)

    class Meta:
        db_table = 'EventsDB_facultades'
    def __str__(self):
        return self.nombre
    
class Empleado(models.Model):
    identificacion = models.CharField(max_length=15, primary_key=True)
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    email = models.EmailField(max_length=40)
    tipo_contratacion = models.CharField(max_length=30)
    tipo_empleado = models.CharField(max_length=30)
    cod_facultad = models.IntegerField()
    codigo_sede = models.IntegerField()
    lugar_nacimiento = models.IntegerField()

    class Meta:
        db_table = 'EventsDB_empleados'  # Asegúrate de que el nombre de la tabla coincida con el de tu base de datos.

    def __str__(self):
        return self.nombres + ' ' + self.apellidos
from django.db import models

class Area(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=40)
    codigo_facultad = models.IntegerField()
    id_coordinador = models.CharField(max_length=15)

class Ciudad(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)
    cod_dpto = models.IntegerField()

class Departamento(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)
    cod_pais = models.IntegerField()

class Empleado(models.Model):
    identificacion = models.CharField(max_length=15, primary_key=True)
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    tipo_contratacion = models.CharField(max_length=30)
    tipo_empleado = models.CharField(max_length=30)
    cod_facultad = models.IntegerField()
    codigo_sede = models.IntegerField()
    lugar_nacimiento = models.IntegerField()

class Facultad(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    ubicacion = models.CharField(max_length=15)
    nro_telefono = models.CharField(max_length=15)
    id_decano = models.CharField(max_length=15)

class Pais(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)

class Programa(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=40)
    codigo_area = models.IntegerField()

class Sede(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)
    cod_ciudad = models.IntegerField()

class TipoContratacion(models.Model):
    nombre = models.CharField(max_length=30, primary_key=True)

class TipoEmpleado(models.Model):
    nombre = models.CharField(max_length=30, primary_key=True)


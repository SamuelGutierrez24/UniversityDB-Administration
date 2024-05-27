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
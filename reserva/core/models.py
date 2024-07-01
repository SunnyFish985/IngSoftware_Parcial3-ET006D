from django.db import models
from distutils.command.upload import upload
# Create your models here.
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name ='Id Categoria')
    nombreCategoria= models.CharField(max_length=40, verbose_name ='Nombre Categoria')

    def __str__(self):
        return self.nombreCategoria

class Transfer(models.Model):
    idVehiculo = models.CharField(primary_key=True, max_length=8, verbose_name ='Id Vehículo')
    patente = models.CharField(max_length = 6, verbose_name='Patente')
    cantAsientos = models.PositiveIntegerField(verbose_name ='Cantidad de Asientos')
    imagen = models.ImageField(upload_to="imagenes",null=True, verbose_name='Imagen')
    disponible = models.BooleanField(default = True, verbose_name='Estado')
    categoria= models.ForeignKey('Categoria', on_delete=models.CASCADE,verbose_name='Categoria')
    idChofer = models.ForeignKey('Chofer', on_delete=models.SET_NULL, null=True, verbose_name='Chofer')

    def __str__(self):
        return self.patente
    
class Chofer(models.Model):
    idChofer = models.IntegerField(primary_key=True, verbose_name='Id Chofer')
    rut = models.IntegerField(verbose_name='Rut')
    dv = models.CharField(max_length = 1, verbose_name='Dígito verificador')
    pNom = models.CharField(max_length= 30, verbose_name='Primer Nombre')
    sNom = models.CharField(max_length= 30, verbose_name='Segundo Nombre')
    pApe = models.CharField(max_length= 30, verbose_name='Primer Apellido')
    sApe = models.CharField(max_length= 30, verbose_name='Segundo Apellido')

    def __str__(self):
        return f"{self.rut}-{self.dv}"




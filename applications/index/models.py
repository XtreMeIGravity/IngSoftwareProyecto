from django.db import models
from ckeditor.fields import RichTextField
from .managers import PublicacionManager
from applications.users.models import User


# Create your models here.

class CatDimensionPlanta(models.Model):
    nombre_DimensionPlanta = models.CharField('DimensionPlanta', max_length=50)

    class Meta:
        verbose_name = "DimensionPlanta"
        verbose_name_plural = "DimensionPlantas"

    def __str__(self):
        return self.nombre_DimensionPlanta


class CatTipoPlanta(models.Model):
    nombre_TipoPlanta = models.CharField('TipoPlanta', max_length=50)

    class Meta:
        verbose_name = "TipoPlanta"
        verbose_name_plural = "TipoPlantas"

    def __str__(self):
        return self.nombre_TipoPlanta


class Planta(models.Model):
    nombre_Planta = models.CharField(max_length=50, unique=True)
    tipo_Planta = models.ForeignKey(CatTipoPlanta, on_delete=models.CASCADE)
    dimension_Planta = models.ForeignKey(CatDimensionPlanta, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_Planta


class CatLugarPlanta(models.Model):
    lugar_Planta = models.CharField('LugarPlanta', max_length=50)

    class Meta:
        verbose_name = "LugarPlanta"
        verbose_name_plural = "LugarPlantas"

    def __str__(self):
        return self.lugar_Planta


class PublicacionesPlantas(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    fotografia_Pub = models.ImageField(upload_to='planta')
    planta_Pub = models.ForeignKey(Planta, on_delete=models.CASCADE)
    fecha_Sembrada = models.DateField()
    lugar_Sembrada_Pub = models.ForeignKey(CatLugarPlanta, on_delete=models.CASCADE)
    sombra = models.BooleanField()
    sol = models.BooleanField()
    cuidados = RichTextField(blank=True, null=True)

    # import manager
    objects = PublicacionManager()

    class Meta:
        ordering = ['-id']


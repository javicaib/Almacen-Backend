from tabnanny import verbose
from django.db import models

# Create your models here.


class BaseModel(models.Model):

    name = models.CharField(max_length=150, verbose_name='Nombre')
    description = models.CharField(max_length=150, verbose_name='Descripcion')

    def __str__(self) -> str:
        return self.name


class Product(BaseModel):

    purchase_price = models.FloatField(verbose_name='Precio de Compra')
    sale_price = models.FloatField(verbose_name='Precio de Venta')

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'



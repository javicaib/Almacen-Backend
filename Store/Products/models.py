from turtle import update
from django.db import models

# Create your models here.


class BaseModel(models.Model):

    name = models.CharField(max_length=150, verbose_name='Nombre')
    state = models.BooleanField(default=True,verbose_name='Estado')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        abstract = True

    def __str__(self) -> str:
        return self.name

MEASURE_CHOICES = [
    ('U', 'Unidad'),
    ('P','Paquete')
]

class Category (BaseModel):
    category_id = models.AutoField(primary_key=True)
    

class Product(BaseModel):

    description = models.CharField(max_length=150, verbose_name='Descripcion')
    purchase_price = models.FloatField(verbose_name='Precio de Compra')
    sale_price = models.FloatField(verbose_name='Precio de Venta')
    measure_unit = models.CharField(verbose_name='Unidad de Medida',choices=MEASURE_CHOICES,max_length=50)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name='Categoria',blank=True)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'


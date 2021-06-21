from django.db import models

# Create your models here.

class Marca(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    description = models.TextField()
    nuevo = models.BooleanField()
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    fecha_fabricacion = models.DateTimeField()
    imagen = models.ImageField(upload_to="productos",null=True) 
    '''Cuando agregamos un nuevo campo al modelo existente, 
    debe ser null o al menos debe tener un valor por defecto,
    porque ya hay datos almacenados en el modelo'''
    def __str__(self):                                          
        return self.nombre
from django.db import models

# Create your models here.

class Category(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    precio = models.IntegerField()
    description = models.TextField()
    disponible = models.BooleanField() 
    fecha_fabricacion = models.DateTimeField()
    imagen = models.ImageField(upload_to="productos",null=True) 
    '''Cuando agregamos un nuevo campo al modelo existente, 
    debe ser null o al menos debe tener un valor por defecto,
    porque ya hay datos almacenados en el modelo'''
    def __str__(self):                                          
        return self.nombre

opciones_consultas = [
    [0, "consulta"],
    [1, "reclamo"],
    [2, "sugerencia"],
    [3, "felicitaciones"]
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField(max_length=50)
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()
    avisos = models.BooleanField()
    def __str__(self):
        return self.nombre
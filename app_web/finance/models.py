import datetime
from django.db import models

class DateTimeModel(models.Model):
    created_at = models.DateTimeField(default = datetime.datetime.now())
    updated_at = models.DateTimeField(default = datetime.datetime.now())
    deleted_at = models.DateTimeField(null = True, blank = True)

    #codicion que nos indica que el modelo no se visible
    class Meta:
        abstract = True

class clientes(DateTimeModel):
    #como puedo factorizar los datos en una sola clase 
    nombre = models.CharField(max_length = 20)
    lastname = models.CharField(max_length = 20)
    email = models.EmailField(null = True, blank = True)
    celular = models.CharField(max_length = 20)

    #Convetir a cadena para que los datos se visualicen 
    def __str__(self):
        return f"{self.nombre}-{self.lastname}-{self.email}-{self.celular}"


class Producto(DateTimeModel):
    nombr_producto = models.CharField(max_length = 50) 
    abreviatura = models.CharField(max_length = 20)
    descripcion = models.CharField(max_length = 100)
    #ident_number = models.CharField(max_length = 12, blank = True) # blank = true que acaepte valores null
    #Crear una llave foranea 
    id_cliente = models.ForeignKey(clientes, on_delete = models.CASCADE)

class cliente_producto(DateTimeModel):
    numero_cuenta= models.IntegerField()
    #id_cliente_Producto = models.ForeignKey(clientes,Producto, on_delete = models.CASCADE)
    id_cliente = models.ForeignKey(clientes, on_delete = models.CASCADE)
    id_producto = models.ForeignKey(Producto, on_delete = models.CASCADE)
    

class Tipo_transancciones(DateTimeModel):
    nombre = models.CharField(max_length = 50) 
    abreviatura = models.CharField(max_length = 20)
    descripcion = models.CharField(max_length = 100)
   
class Transaccion(DateTimeModel):
    monto = models.IntegerField() 
    id_cliente_producto = models.ForeignKey(cliente_producto, on_delete = models.CASCADE)
    id_transaccion = models.ForeignKey(Tipo_transancciones, on_delete = models.CASCADE)


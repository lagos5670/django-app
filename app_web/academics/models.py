import datetime
from django.db import models


class DateTimeModel(models.Model):
    created_at = models.DateTimeField(default = datetime.datetime.now())
    updated_at = models.DateTimeField(default = datetime.datetime.now())
    deleted_at = models.DateTimeField(null = True, blank = True)

    #codicion que nos indica que el modelo no se visible
    class Meta:
        abstract = True



    

# Create your models here.
#model.DateTimeField(auto_now = true, null = false ) => update_at
#model.DateTimeField(auto_now_add = true, null = false ) => Defaul now()
#usamos models.Model para usar los timpos de campos ejemplos variables
class User(DateTimeModel):
    #como puedo factorizar los datos en una sola clase 
    email = models.EmailField(null = True, blank = True)
    password = models.CharField(null = True, blank = True)
    status = models.BooleanField(null = True, blank = True, default = True)
   

    #Convetir a acdena para que los datos se visualicen 
    def __str__(self):
        return f" {self.email}-{self.password}"


class Person(DateTimeModel):
    firstname = models.CharField(max_length = 20) 
    lastname = models.CharField(max_length = 20)
    age = models.IntegerField()
    ident_number = models.CharField(max_length = 12, blank = True) # blank = true que acaepte valores null
    #Crear una llave foranea 
    id_user = models.ForeignKey(User, on_delete = models.CASCADE, default =1)


class Students(DateTimeModel):
    code = models.CharField(max_length = 20)
    status = models.BooleanField(null = True, blank = True, default = True)
    

class identification_types(DateTimeModel):
    name = models.CharField(max_length = 50)
    abrev = models.CharField(max_length = 10)
    descrip =  models.CharField(max_length = 100)
   

class cities(DateTimeModel):
    name = models.CharField(max_length = 100)
    abrev = models.CharField(max_length = 10)
    descrip =  models.CharField(max_length = 10)


class departments(DateTimeModel):
    name = models.CharField(max_length = 100)
    abrev = models.CharField(max_length = 10)
    descrip =  models.CharField(max_length = 10)
   

class countries(DateTimeModel):
    name = models.CharField(max_length = 100)
    abrev = models.CharField(max_length = 10)
    descrip =  models.CharField(max_length = 10)
    

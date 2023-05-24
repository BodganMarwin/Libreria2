from django.db import models

# Create your models here.

class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

class Author(models.Model):
    salutation = models.CharField(max_length=10)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    headshot = models.ImageField(upload_to='tmp')

class Book(models.Model):
    title=models.CharField(max_length=100)
    # authors = models.ManyToManyField(Author)
    # publisher=models.ForeignKey(Publisher)
    publication_date=models.DateField()

#####################


class Clientes(models.Model):
    nombre=models.CharField(max_length=30, help_text='Nombre del cliente')
    direccion=models.CharField(max_length=50, verbose_name='Direccion del cliente')
    email=models.EmailField(blank=True,null=True)
    telefono=models.CharField(max_length=8, )

    def __str__(self):
        return self.nombre

class Articulos(models.Model):
    nombre=models.CharField(max_length=30)
    seccion=models.CharField(max_length=20)
    precio=models.IntegerField()

    def __str__(self):

        return 'El nombre es %s la seccion es %s y el precio es %s'%(self.nombre,self.seccion,self.precio)

class Pedidos(models.Model):
    numero=models.IntegerField()
    fecha=models.DateField()
    entregado=models.BooleanField()

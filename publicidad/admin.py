from django.contrib import admin

from publicidad.models import Clientes, Author,Pedidos, Articulos

# Register your models here.

admin.site.register(Clientes)
admin.site.register(Author)
admin.site.register(Pedidos)
admin.site.register(Articulos)

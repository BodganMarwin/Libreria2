from django.contrib import admin

from publicidad.models import Clientes, Author,Pedidos, Articulos

# Register your models here.

class ClientesAdmin(admin.ModelAdmin):
    list_display=('nombre','direccion','telefono')
    search_fields=('nombre', 'telefono')

class ArticulosAdmin(admin.ModelAdmin):
    list_filter=('seccion',)

class PedidosAdmin(admin.ModelAdmin):
    list_display=('numero','fecha','entregado')
    list_filter=('fecha',)
    date_hierarchy='fecha'

admin.site.register(Clientes, ClientesAdmin)
admin.site.register(Author)
admin.site.register(Pedidos,PedidosAdmin)
admin.site.register(Articulos,ArticulosAdmin)

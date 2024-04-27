
from django.contrib import admin
from .models import clientes,Producto,cliente_producto,Tipo_transancciones,Transaccion
# Register your models here.
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre','lastname','email','celular','created_at','updated_at','deleted_at')


class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombr_producto','abreviatura','descripcion','id_cliente','created_at','updated_at','deleted_at')


class Cliente_productoAdmin(admin.ModelAdmin):
    list_display = ('numero_cuenta','id_cliente','id_producto','created_at','updated_at','deleted_at')


class TipoTransaccionAdmin(admin.ModelAdmin):
    list_display = ('nombre','abreviatura','descripcion','created_at','updated_at','deleted_at')

class TransaccionAdmin(admin.ModelAdmin):
    list_display = ('monto','id_cliente_producto','id_transaccion','created_at','updated_at','deleted_at')

admin.site.register(clientes, ClienteAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(cliente_producto, Cliente_productoAdmin)
admin.site.register(Tipo_transancciones, TipoTransaccionAdmin)
admin.site.register(Transaccion, TransaccionAdmin)



# Register your models here.

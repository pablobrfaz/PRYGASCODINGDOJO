from django.contrib import admin
from .models import (Direccion,
User,
Producto,
Bodega,
Factura,
Detalle_Venta)

admin.site.register(User)
admin.site.register(Direccion)
admin.site.register(Producto)
admin.site.register(Bodega)
admin.site.register(Factura)
admin.site.register(Detalle_Venta)
# Register your models here.

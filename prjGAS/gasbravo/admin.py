from django.contrib import admin
from .models import (Direccion,
User,
Producto,
Bodega,
)

admin.site.register(User)
admin.site.register(Direccion)
admin.site.register(Producto)
admin.site.register(Bodega)
#admin.site.register(Status_Ped)
#admin.site.register(Pedido)
#admin.site.register(Pedido_prod)
# Register your models here.

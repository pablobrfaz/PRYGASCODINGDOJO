from os import name
from django.urls import path
from . import views


urlpatterns = [
    #Views Login Crear Usuarios 
    path('', views.index),
    path('user/create_user', views.create_user),
    path('user/login', views.login),
    path('logout', views.logout),
    path('user/logout', views.logout),
    
    path('user/dashboard',views.dashboard_rol),
    #Views Direcciones
    path('user/gest_direccion',views.gest_direccion),
    path('user/add_direccion',views.createAddress),
    path('user_dir/<int:number>/edit', views.edit_dir),
    path('user_dir/update/<int:number>',views.edit_dir),
    path('user_dir/<int:number>/delete',views.delete_dir),
    #Views Usuarios
    path('user/create_users', views.create_users),
    path('user/gestion_users',views.gest_users),
    path('user_usr/<int:number>/edit', views.edit_usr),
    path('user_usr/update/<int:number>',views. edit_usr),
    path('user_cli/<int:number>/edit', views.edit_usr_cl),
    path('user_cli/update/<int:number>',views. edit_usr_cl),
    path('user/<int:number>/delete',views.delete_user),
    #Views Productos    
    path('user/create_prod', views.create_prod),
    path('user/gestion_prod',views.gest_prod),
    path('user_prd/<int:number>/edit', views.edit_prd),
    path('user_prd/update/<int:number>',views. edit_prd),
    path('user_prod/<int:number>/delete',views.delete_prod),

    #Views Bodegas
    path('user/create_bodega', views.create_bod),
    path('user/gestion_bodega',views.gest_bod),
    path('user_bod/<int:number>/delete',views.delete_bod),
    
    #test
    path('user/test', views.test),
    # Pedidos
    path('user/create_pedido', views.crear_pedido),
    path('user/procesar_pedido', views.procesar_pedido),
    path('user/cancelar_pedido/<int:id_pedido>', views.cancelar_pedido),
    path('user/pedidos',  views.mostrar_pedidos),

    #sending email
    path('user/sending', views.sendmesa),

    #creating pdf
    path('user/invoice', views.invoice_pdf_view),

]

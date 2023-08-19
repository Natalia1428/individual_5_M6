from django.urls import path

from app.views import vista_index, vista_clientes, vista_registroCliente, vista_login, custom_logout


urlpatterns = [
    path('', vista_index, name='index'),
    path('clientes/', vista_clientes, name='clientes'),
    path('registroClientes/', vista_registroCliente, name='registroCliente'),
    path('login/', vista_login, name='login'),
    path('logout/', custom_logout, name='logout'),
  
]
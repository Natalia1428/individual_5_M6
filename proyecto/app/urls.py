from django.urls import path

from app.views import vista_index, vista_usuarios, vista_registroUsuario, vista_login, custom_logout


urlpatterns = [
    path('', vista_index, name='index'),
    path('usuarios/', vista_usuarios, name='usuarios'),
    path('registroUsuario/', vista_registroUsuario, name='registroUsuario'),
    path('login/', vista_login, name='login'),
    path('logout/', custom_logout, name='logout'),
  
]
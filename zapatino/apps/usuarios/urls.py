from django.conf.urls import url
from apps.usuarios import views 



urlpatterns = [
    url(r'^apps.usuarios/registrar/$', views.registrar, name = "registrar"),
    
   # url(r'^apps.usuarioslogin/login/$', views.login_us, name = "login"),
   url(r'^login/$','django.contrib.auth.views.login', name = "login"),
  
      
    url(r'^cerrar/$','django.contrib.auth.views.logout_then_login', name = "logout"),
 ]



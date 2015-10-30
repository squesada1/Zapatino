from django.conf.urls import url
from apps.zapatino_shop import views 

urlpatterns = [
    url(r'^$', views.formulario_index, name="formulario_index"),                
    url(r'^apps.zapatino/empresa$', views.formulario_empresa, name="formulario_empresa"),
      
]
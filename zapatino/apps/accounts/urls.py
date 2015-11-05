from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^apps.accounts/registrar_usuario$', views.registro_usuario_view, name='registro_usuario_view'),
]
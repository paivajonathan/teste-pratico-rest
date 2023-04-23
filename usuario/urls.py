from django.urls import path
from usuario.api.viewsets import UsuarioCreateView


urlpatterns = [
    path('registrar/', UsuarioCreateView.as_view(), name='user_create'),
]
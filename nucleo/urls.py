"""
URL configuration for nucleo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from endereco.api.viewsets import EnderecoViewSet
from empresa.api.viewsets import EmpresaViewSet
from veiculo.api.viewsets import VeiculoViewSet


router = routers.DefaultRouter()
router.register(r'endereco', EnderecoViewSet)
router.register(r'empresa', EmpresaViewSet)
router.register(r'veiculo', VeiculoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('', include('rest_framework.urls')),
    path('', include('usuario.urls')),
    path('empresa/<int:pk>/veiculos', EmpresaViewSet.as_view({'get': 'list_veiculos'}), name='list_veiculos'),
    path('empresa/cnpj/<str:cnpj>/', EmpresaViewSet.as_view({'get': 'retrieve_by_cnpj'}), name='retrieve_by_cnpj'),
    path('empresa/detalhes/<str:pk_cnpj>/', EmpresaViewSet.as_view({'get': 'retrieve_details'}), name='retrieve_details'),
]

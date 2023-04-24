from django.urls import path
from empresa.api.viewsets import EmpresaViewSet


urlpatterns = [
    path('<int:pk>/veiculos/', EmpresaViewSet.as_view({'get': 'list_veiculos'}), name='list_veiculos'),
    path('cnpj/<str:cnpj>/', EmpresaViewSet.as_view({'get': 'retrieve_by_cnpj'}), name='retrieve_by_cnpj'),
    path('detalhes/<str:pk_cnpj>/', EmpresaViewSet.as_view({'get': 'retrieve_details'}), name='retrieve_details'),   
]
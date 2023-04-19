from rest_framework.viewsets import ModelViewSet
from empresa.models import Empresa
from empresa.api.serializers import EmpresaSerializer
from rest_framework.pagination import PageNumberPagination


class EmpresaViewSet(ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    pagination_class = PageNumberPagination
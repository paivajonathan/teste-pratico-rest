from rest_framework.viewsets import ModelViewSet
from empresa.models import Empresa
from empresa.api.serializers import EmpresaSerializer


class EmpresaViewSet(ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
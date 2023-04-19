from rest_framework.viewsets import ModelViewSet
from veiculo.models import Veiculo
from veiculo.api.serializers import VeiculoSerializer
from rest_framework.pagination import PageNumberPagination


class VeiculoViewSet(ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer
    pagination_class = PageNumberPagination
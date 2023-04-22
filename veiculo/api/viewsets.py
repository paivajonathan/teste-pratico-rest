from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from veiculo.models import Veiculo
from veiculo.api.serializers import VeiculoSerializer


class VeiculoViewSet(ModelViewSet):
    queryset = Veiculo.objects.all().order_by('id')
    serializer_class = VeiculoSerializer
    pagination_class = PageNumberPagination
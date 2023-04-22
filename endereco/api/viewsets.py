from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from endereco.models import Endereco
from endereco.api.serializers import EnderecoSerializer


class EnderecoViewSet(ModelViewSet):
    queryset = Endereco.objects.all().order_by('id')
    serializer_class = EnderecoSerializer
    pagination_class = PageNumberPagination
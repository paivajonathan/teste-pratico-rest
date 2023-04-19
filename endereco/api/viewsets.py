from rest_framework.viewsets import ModelViewSet
from endereco.models import Endereco
from endereco.api.serializers import EnderecoSerializer
from rest_framework.pagination import PageNumberPagination


class EnderecoViewSet(ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer
    pagination_class = PageNumberPagination
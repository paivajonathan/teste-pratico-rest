from rest_framework.viewsets import ModelViewSet
from empresa.models import Empresa
from veiculo.models import Veiculo
from empresa.api.serializers import EmpresaSerializer
from veiculo.api.serializers import VeiculoSerializer
from endereco.api.serializers import EnderecoSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response


class EmpresaViewSet(ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    pagination_class = PageNumberPagination

    @action(detail=False, methods=['get'], url_path='cnpj/(?P<cnpj>[^/.]+)')
    def retrieve_by_cnpj(self, request, cnpj=None):
        try:
            empresa = Empresa.objects.get(vCnpj=cnpj)
        except Empresa.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = EmpresaSerializer(empresa)
        return Response(serializer.data)
    
    @action(detail=True, methods=['get'], url_path='veiculos')
    def list_veiculos(self, request, pk=None):
        empresa = self.get_object()
        veiculos = Veiculo.objects.filter(iCod_empresa=empresa).order_by('id')

        paginator = PageNumberPagination()
        paginator.page_size = 2
        page = paginator.paginate_queryset(veiculos, request)

        serializer = VeiculoSerializer(page, many=True)
        empresa_serializer = EmpresaSerializer(empresa)

        return Response({
            'empresa': empresa_serializer.data,
            'veiculos': serializer.data,
            'pagination': {
                'next': paginator.get_next_link(),
                'previous': paginator.get_previous_link()
            }
        })

    @action(detail=True, methods=['get'], url_path='detalhes/(?P<pk_cnpj>[^/.]+)')
    def retrieve_details(self, request, pk_cnpj=None):
        try:
            if len(pk_cnpj) < 14:
                empresa = Empresa.objects.get(pk=pk_cnpj)
            else:
                empresa = Empresa.objects.get(vCnpj=pk_cnpj)
        except Empresa.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        empresa_serializer = EmpresaSerializer(empresa)
        endereco_serializer = EnderecoSerializer(empresa.iCod_endereco)

        return Response({
            'empresa': empresa_serializer.data,
            'endereco': endereco_serializer.data
        })

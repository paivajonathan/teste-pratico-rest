from rest_framework.viewsets import ModelViewSet
from empresa.models import Empresa
from veiculo.models import Veiculo
from empresa.api.serializers import EmpresaSerializer
from veiculo.api.serializers import VeiculoSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response


class EmpresaViewSet(ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    pagination_class = PageNumberPagination

    @action(detail=False, methods=['get'], url_path='cnpj/(?P<cnpj>[^/.]+)', url_name='consulta_por_cnpj')
    def consulta_por_cnpj(self, request, cnpj=None):
        try:
            empresa = Empresa.objects.get(vCnpj=cnpj)
        except Empresa.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = EmpresaSerializer(empresa)
        return Response(serializer.data)
    
    @action(detail=True, methods=['get'])
    def veiculos(self, request, pk=None):
        empresa = self.get_object()
        veiculos = Veiculo.objects.filter(iCod_empresa=empresa)

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
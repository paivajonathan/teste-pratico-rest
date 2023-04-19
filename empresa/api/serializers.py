from rest_framework.serializers import ModelSerializer
from empresa.models import Empresa


class EmpresaSerializer(ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'
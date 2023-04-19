from rest_framework.serializers import ModelSerializer
from veiculo.models import Veiculo


class VeiculoSerializer(ModelSerializer):
    class Meta:
        model = Veiculo
        fields = '__all__'
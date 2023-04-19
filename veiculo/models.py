from django.db import models
from empresa.models import Empresa


class Veiculo(models.Model):
    vDesc_veiculo = models.CharField(max_length=35)
    vPlaca = models.CharField(max_length=7)
    nValor = models.DecimalField(max_digits=15, decimal_places=3)
    iCod_empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    def __str__(self):
        return f'Placa: {self.vPlaca}'
from django.db import models
from django.core.validators import RegexValidator
from empresa.models import Empresa


class Veiculo(models.Model):
    vDesc_veiculo = models.CharField(max_length=35)
    vPlaca = models.CharField(max_length=7, validators=[RegexValidator(regex=r'^[A-Z]{3}\d[A-Z0-9]{2}\d$', message='A placa deve seguir o formato LLLNLNN.')])
    nValor = models.DecimalField(max_digits=15, decimal_places=3)
    iCod_empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    def __str__(self):
        return f'Placa: {self.vPlaca}'
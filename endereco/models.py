from django.db import models
from django.core.validators import RegexValidator


class Endereco(models.Model):
    vLogradouro = models.CharField(max_length=80)
    vComplemento = models.CharField(max_length=50)
    vBairro = models.CharField(max_length=40)
    vNumero = models.CharField(max_length=10, validators=[RegexValidator(regex=r'^[0-9]*$', message='Somente números são permitidos.')])
    cUF = models.CharField(max_length=2, validators=[RegexValidator(regex=r'^[A-Z]{2}$', message='O campo cUF deve ter exatamente dois caracteres maiúsculos.')])

    def __str__(self):
        return f'Logradouro: {self.vLogradouro}, Complemento: {self.vComplemento}, Bairro: {self.vBairro}, Numero: {self.vNumero}, UF: {self.cUF}'
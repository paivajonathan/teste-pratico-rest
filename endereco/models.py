from django.db import models
from django.core.validators import RegexValidator, MinLengthValidator


class Endereco(models.Model):
    vLogradouro = models.CharField(max_length=80)
    vComplemento = models.CharField(max_length=50)
    vBairro = models.CharField(max_length=40)
    vNumero = models.CharField(max_length=10, validators=[RegexValidator(r'^[0-9]*$', 'Somente números são permitidos.')])
    cUF = models.CharField(max_length=2, validators=[MinLengthValidator(2, 'Este campo deve ter 2 caracteres.')])

    def __str__(self):
        return f'Logradouro: {self.vLogradouro}, Complemento: {self.vComplemento}, Bairro: {self.vBairro}, Numero: {self.vNumero}, UF: {self.cUF}'
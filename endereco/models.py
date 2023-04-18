from django.db import models


class Endereco(models.Model):
    vLogradouro = models.CharField(max_length=80)
    vComplemento = models.CharField(max_length=50)
    vBairro = models.CharField(max_length=40)
    vNumero = models.CharField(max_length=10)
    cUF = models.CharField(max_length=2)

    def __str__(self):
        return f'Logradouro: {self.vLogradouro}, Complemento: {self.vComplemento}, Bairro: {self.vBairro}, Numero: {self.vNumero}, UF: {self.cUF}'
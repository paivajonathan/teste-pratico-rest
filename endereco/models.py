from django.db import models


class Endereco(models.Model):
    vLogradouro = models.CharField(80)
    vComplemento = models.CharField(50)
    vBairro = models.CharField(40)
    vNumero = models.CharField(10)
    cUF = models.CharField(2)

    def __str__(self):
        return f'Logradouro: {self.vLogradouro}, Complemento: {self.vComplemento}, Bairro: {self.vBairro}, Numero: {self.vNumero}, UF: {self.cUF}'
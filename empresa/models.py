from django.db import models
from django.core.validators import RegexValidator, EmailValidator
from endereco.models import Endereco


class Empresa(models.Model):
    vNome_fantasia = models.CharField(max_length=80)
    vNome_razao_social = models.CharField(max_length=80)
    vCnpj = models.CharField(max_length=14, validators=[RegexValidator(r'^\d{14}$', 'O CNPJ deve conter 14 dígitos.')])
    vEmail = models.CharField(max_length=40, validators=[EmailValidator(message='Digite um email válido.')])
    vObservacao = models.CharField(max_length=200)
    iCod_endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE, error_messages={ 'unique': 'Endereço já cadastrado.' })

    def __str__(self):
        return f'Nome fantasia: {self.vNome_fantasia}, Razao social: {self.vNome_razao_social}'
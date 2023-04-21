from rest_framework.test import APITestCase
from rest_framework import status
from endereco.models import Endereco
from empresa.models import Empresa
from veiculo.models import Veiculo
from django.contrib.auth.models import User
from rest_framework.test import APIClient


class EnderecoViewSetTestCase(APITestCase):
    
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_superuser(username='superuser', password='12345')
        self.enderecoA = Endereco.objects.create(vLogradouro='Rua A', vComplemento='Complemento A', vBairro='Bairro A', vNumero='100', cUF='PI')
        self.empresaA = Empresa.objects.create(vNome_fantasia='Empresa A', vNome_razao_social='Empresa A', vCnpj='12345678909876', vEmail='empresaa@gmail.com', vObservacao='Observacao A', iCod_endereco=self.enderecoA)
        self.veiculoA = Veiculo.objects.create(vDesc_veiculo='Veiculo A', vPlaca='LXC4Z67', nValor=20000.920, iCod_empresa=self.empresaA)
        self.veiculoB = Veiculo.objects.create(vDesc_veiculo='Veiculo B', vPlaca='FMG3P75', nValor=10000.990, iCod_empresa=self.empresaA)

    def test_list_veiculos(self):
        self.client.login(username='superuser', password='12345')
        response = self.client.get('/veiculo/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_retrieve_veiculo(self):
        self.client.login(username='superuser', password='12345')
        response = self.client.get(f'/veiculo/{self.veiculoA.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_veiculo(self):
        self.client.login(username='superuser', password='12345')
        data = { 
            'vDesc_veiculo': 'Veiculo C',
            'vPlaca': 'ABC6D78',
            'nValor': 50000.100, 
            'iCod_empresa': self.empresaA.id 
        }
        response = self.client.post('/veiculo/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_veiculo(self):
        self.client.login(username='superuser', password='12345')
        data = { 
            'vDesc_veiculo': 'Veiculo D',
            'vPlaca': 'HIJ9D25',
            'nValor': 45000.000, 
            'iCod_empresa': self.empresaA.id 
        }
        response = self.client.put(f'/veiculo/{self.veiculoA.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_veiculo(self):
        self.client.login(username='superuser', password='12345')
        response = self.client.delete(f'/veiculo/{self.veiculoB.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
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
        self.enderecoB = Endereco.objects.create(vLogradouro='Rua B', vComplemento='Complemento B', vBairro='Bairro B', vNumero='200', cUF='MA')
        self.enderecoC = Endereco.objects.create(vLogradouro='Rua C', vComplemento='Complemento C', vBairro='Bairro C', vNumero='300', cUF='CE')
        
        self.empresaA = Empresa.objects.create(vNome_fantasia='Empresa A', vNome_razao_social='Empresa A', vCnpj='12345678909876', vEmail='empresaa@gmail.com', vObservacao='Observacao A', iCod_endereco=self.enderecoA)
        self.empresaB = Empresa.objects.create(vNome_fantasia='Empresa B', vNome_razao_social='Empresa B', vCnpj='09876543212345', vEmail='empresab@gmail.com', vObservacao='Observacao B', iCod_endereco=self.enderecoB)

        self.veiculoA = Veiculo.objects.create(vDesc_veiculo='Veiculo A', vPlaca='LXC4Z67', nValor=20000.920, iCod_empresa=self.empresaB)
        self.veiculoB = Veiculo.objects.create(vDesc_veiculo='Veiculo B', vPlaca='FMG3P75', nValor=10000.990, iCod_empresa=self.empresaB)

    def test_list_empresas(self):
        self.client.login(username='superuser', password='12345')
        response = self.client.get('/empresa/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_retrieve_empresa(self):
        self.client.login(username='superuser', password='12345')
        response = self.client.get(f'/empresa/{self.empresaA.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_retrieve_empresa_by_cnpj(self):
        self.client.login(username='superuser', password='12345')
        response = self.client.get(f'/empresa/cnpj/{self.empresaA.vCnpj}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_veiculos(self):
        self.client.login(username='superuser', password='12345')
        response = self.client.get(f'/empresa/{self.empresaB.id}/veiculos/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_retrieve_details_id(self):
        self.client.login(username='superuser', password='12345')
        response = self.client.get(f'/empresa/detalhes/{self.empresaB.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_details_cnpj(self):
        self.client.login(username='superuser', password='12345')
        response = self.client.get(f'/empresa/detalhes/{self.empresaB.vCnpj}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_retrieve_empresa_by_part_of_name(self):
        self.client.login(username='superuser', password='12345')
        response = self.client.get(f'/empresa/?search={self.empresaB.vNome_fantasia[0:5]}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_empresa(self):
        self.client.login(username='superuser', password='12345')
        data = { 
            'vNome_fantasia': 'Empresa C', 
            'vNome_razao_social': 'Empresa C', 
            'vCnpj': '10293847564738', 
            'vEmail': 'empresac@gmail.com', 
            'vObservacao': 'Observacao C', 
            'iCod_endereco': self.enderecoC.id
        }
        response = self.client.post('/empresa/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_empresa(self):
        self.client.login(username='superuser', password='12345')
        data = { 
            'vNome_fantasia': 'Empresa D', 
            'vNome_razao_social': 'Empresa D', 
            'vCnpj': '01928374657483', 
            'vEmail': 'empresad@gmail.com', 
            'vObservacao': 'Observacao D', 
            'iCod_endereco': self.enderecoA.id
        }
        response = self.client.put(f'/empresa/{self.empresaA.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_empresa(self):
        self.client.login(username='superuser', password='12345')
        response = self.client.delete(f'/empresa/{self.empresaB.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

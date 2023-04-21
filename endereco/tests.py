from rest_framework.test import APITestCase
from rest_framework import status
from endereco.models import Endereco
from django.contrib.auth.models import User
from rest_framework.test import APIClient


class EnderecoViewSetTestCase(APITestCase):
    
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_superuser(username='superuser', password='12345')
        self.enderecoA = Endereco.objects.create(vLogradouro='Rua A', vComplemento='Complemento A', vBairro='Bairro A', vNumero='100', cUF='PI')
        self.enderecoB = Endereco.objects.create(vLogradouro='Rua B', vComplemento='Complemento B', vBairro='Bairro B', vNumero='200', cUF='MA')

    def test_list_enderecos(self):
        self.client.login(username='superuser', password='12345')
        response = self.client.get('/endereco/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_endereco(self):
        self.client.login(username='superuser', password='12345')
        data = { 
            'vLogradouro': 'Rua C', 
            'vComplemento': 'Complemento C', 
            'vBairro': 'Bairro C', 
            'vNumero': '300', 
            'cUF': 'CE' 
        }
        response = self.client.post('/endereco/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_endereco(self):
        self.client.login(username='superuser', password='12345')
        data = { 
            'vLogradouro': 'Rua C', 
            'vComplemento': 'Complemento C', 
            'vBairro': 'Bairro C', 
            'vNumero': '300', 
            'cUF': 'CE' 
        }
        response = self.client.put(f'/endereco/{self.enderecoA.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_endereco(self):
        self.client.login(username='superuser', password='12345')
        response = self.client.delete(f'/endereco/{self.enderecoB.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

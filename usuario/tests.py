from rest_framework.test import APITestCase, APIClient
from rest_framework import status


class UsuarioViewSetTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
    
    def test_create_usuario(self):
        data = {
            "username": "UsuarioA",
            "password": "A@123"
        }
        response = self.client.post('/registrar/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_authenticate_usuario(self):
        data = {
            "username": "UsuarioA",
            "password": "A@123"
        }
        response = self.client.post('/login/?next=/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
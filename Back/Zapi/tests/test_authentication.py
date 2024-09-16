from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate
from django.urls import reverse
from rest_framework import status

class AuthenticationUserTestCase(APITestCase):
    def setUp(self):
        self.usuario = User.objects.create_superuser(username='admin', password='admin')
        self.url = reverse('Companies-list')

    def test_autenticacao_credencial_correta(self):
        usuario = authenticate(username = 'admin', password='admin')
        self.assertTrue((usuario is not None) and usuario.is_authenticated)
    
    def test_autenticacao_username_incorreto(self):
        usuario = authenticate(username = 'admn', password='admin')
        self.assertFalse((usuario is not None) and usuario.is_authenticated)

    def test_autenticacao_senha_incorreta(self):
        usuario = authenticate(username = 'admin', password='adm')
        self.assertFalse((usuario is not None) and usuario.is_authenticated)

    def test_requisicao_get(self):
        self.client.force_authenticate(self.usuario)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
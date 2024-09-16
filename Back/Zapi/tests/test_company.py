from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from Zapi.models import Company
from Zapi.serializers import CompanySerializer

class CompanyTestCase(APITestCase):
    def setUp(self):
        self.usuario = User.objects.create_superuser(username='admin', password='admin')
        self.url = reverse('Companies-list')
        self.client.force_authenticate(user = self.usuario)
        self.company = Company.objects.create(
            name = 'Empresa Company',
            created_at = '2024-09-15T23:27:51.076371-03:00',
            last_updated_at = '2024-09-15T23:27:51.076371-03:00'
        )

    def test_get_companies(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_company(self):
        detail_url = reverse('Companies-detail', kwargs={'pk': self.company.id})
        response = self.client.get(detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        company = Company.objects.get(pk=self.company.id)
        company_serializada = CompanySerializer(instance=company).data
        self.assertEqual(response.data, company_serializada)

    def test_post_company(self):
        request = {
            'name': 'Empresa Company',
            'created_at': '2024-09-15T23:27:51.076371-03:00',
            'last_updated_at': '2024-09-15T23:27:51.076371-03:00'
        }

        response = self.client.post(self.url, data=request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_company(self):
        response = self.client.delete(f'{self.url}/{self.company.id}')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_put_company(self):
        request = {
            'name': 'Empresa Atualizada',
            'created_at': '2024-09-15T23:27:51.076371-03:00',
            'last_updated_at': '2024-09-17T23:27:51.076371-03:00'
        }

        response = self.client.put(f'{self.url}/{self.company.id}', data=request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
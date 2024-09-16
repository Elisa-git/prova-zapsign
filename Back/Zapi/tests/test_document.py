from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from Zapi.models import Document, Company
from Zapi.serializers import DocumentSerializer

class DocumentTestCase(APITestCase):
    def setUp(self):
        self.usuario = User.objects.create_superuser(username='admin', password='admin')
        self.url = reverse('Documents-list')
        self.client.force_authenticate(user = self.usuario)
        
        self.company = Company.objects.create(
            name = 'Empresa company'
        )

        self.document = Document.objects.create(
            name = 'Documento Um',
            status = 'Novo',
            created_by = 'Fulano de Tal',
            companyId = self.company,
            openId = 123
        )

    def test_get_documents(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_document(self):
        detail_url = reverse('Documents-detail', kwargs={'pk': self.document.id})
        response = self.client.get(detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        document = Document.objects.get(pk=self.document.id)
        document_serializado = DocumentSerializer(instance=document).data
        self.assertEqual(response.data, document_serializado)

    def test_delete_document(self):
        response = self.client.delete(f'{self.url}/{self.document.id}')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
    def test_put_document(self):
        request = {
            'name': 'Documento Um Dois',
            'status': 'Novo',
            'created_by': 'Fulano de Tal',
            'companyId': self.company,
            'openId': 123
        }

        response = self.client.put(f'{self.url}/{self.document.id}', data=request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_post_document(self):
        request = {
            'name': 'Documento Um',
            'openId': 123,
            'status': 'Novo',
            'created_by': 'Fulano de Tal',
            'companyId': self.company.pk,
            'token': '123',
        }

        response = self.client.post(self.url, data=request, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
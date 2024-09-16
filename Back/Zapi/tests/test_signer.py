from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from Zapi.models import Document, Company, Signer
from Zapi.serializers import SignerSerializer
from django.conf import settings

class SignerTestCase(APITestCase):
    def setUp(self):
        self.usuario = User.objects.create_superuser(username='admin', password='admin')
        self.url = reverse('Signers-list')
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

        self.signer = Signer.objects.create(
            token = '123',
            status = 'Novo',
            name = 'Fulano',
            email = 'fula@email.com',
            externalId = settings.API_TOKEN,
            documentId = self.document
        )

    def test_get_signers(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_signer(self):
        detail_url = reverse('Signers-detail', kwargs={'pk': self.signer.id})
        response = self.client.get(detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        signer = Signer.objects.get(pk=self.signer.id)
        signer_serializado = SignerSerializer(instance=signer).data
        self.assertEqual(response.data, signer_serializado)

    def test_delete_signer(self):
        response = self.client.delete(f'{self.url}/{self.signer.id}')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_put_signer(self):
        request = {
            'token': '123',
            'status': 'Novo',
            'name': 'Fulano',
            'email': 'fula@email.com',
            'externalId': settings.API_TOKEN,
            'documentId': self.document.pk
        }

        response = self.client.put(f'{self.url}/{self.signer.id}', data=request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_signer(self):
        request = {
            'token': '1123',
            'status': 'Novo neditado',
            'name': 'Fulano',
            'email': 'fula@email.com',
            'externalId': settings.API_TOKEN,
            'documentId': self.document.pk
        }

        response = self.client.post(self.url, data=request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
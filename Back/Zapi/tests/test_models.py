from django.test import TestCase
from Zapi.models import Company, Document, Signer
import datetime
from django.conf import settings

class ModelCompanyTestCase(TestCase):

    def setUp(self):

        self.company = Company.objects.create(
            name = 'Empresa company'
        )

    def test_verifica_atributos_company(self):

        company_compare = {
            'name': 'Empresa company',
            'created_at': datetime.datetime(2024, 9, 16, 2, 27, 51, 76371, tzinfo=datetime.timezone.utc),
            'last_updated_at': datetime.datetime(2024, 9, 16, 2, 27, 51, 76371, tzinfo=datetime.timezone.utc),
            'api_token': settings.API_TOKEN
        }
        self.assertEqual(self.company.name, company_compare['name'])
        self.assertEqual(self.company.api_token, company_compare['api_token'])


class ModelDocumentTestCase(TestCase):
    def setUp(self):

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

    def test_verifica_atributos_document(self):
        document_compare = {
            'name': 'Documento Um',
            'status': 'Novo',
            'created_by': 'Fulano de Tal',
            'companyId': self.company,
            'openId': 123
        }

        self.assertEqual(self.document.name, document_compare['name'])
        self.assertEqual(self.document.status, document_compare['status'])
        self.assertEqual(self.document.created_by, document_compare['created_by'])
        self.assertEqual(self.document.companyId, document_compare['companyId'])
        self.assertEqual(self.document.openId, document_compare['openId'])

class ModelSignerTestCase(TestCase):
    def setUp(self):
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
    
    def test_verifica_atributos_signer(self):
        signer_compare = {
            'token': '123',
            'status': 'Novo',
            'name': 'Fulano',
            'email': 'fula@email.com',
            'externalId': settings.API_TOKEN,
            'documentId': self.document
        }

        self.assertEqual(self.signer.token, signer_compare['token'])
        self.assertEqual(self.signer.status, signer_compare['status'])
        self.assertEqual(self.signer.name, signer_compare['name'])
        self.assertEqual(self.signer.email, signer_compare['email'])
        self.assertEqual(self.signer.externalId, signer_compare['externalId'])
        self.assertEqual(self.signer.documentId, signer_compare['documentId'])




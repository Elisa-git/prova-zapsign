from django.test import TestCase
from Zapi.models import Company
from Zapi.serializers import CompanySerializer
import datetime
from django.conf import settings

class SerializerCompanyTestCase(TestCase):
    
    def setUp(self):
        self.company = Company (
            name = 'Empresa company',
            created_at = '2024-09-15T23:27:51.076371-03:00',
            last_updated_at = '2024-09-15T23:27:51.076371-03:00',
            api_token = settings.API_TOKEN
        )

        self.serializer_company = CompanySerializer(instance=self.company)

    def test_verifica_conteudo_campos_serializados_company(self):
        dados = self.serializer_company.data
        self.assertSetEqual(set(dados.keys()), set(['name', 'created_at', 'last_updated_at', 'api_token', 'id']))

    def test_verifica_company_name(self):
        dados = self.serializer_company.data
        self.assertEqual(dados['name'], self.company.name)

    def test_verifica_company_created_at(self):
        dados = self.serializer_company.data
        self.assertEqual(dados['created_at'], self.company.created_at)

    def test_verifica_company_last_updated_at(self):
        dados = self.serializer_company.data
        self.assertEqual(dados['last_updated_at'], self.company.last_updated_at)

    def test_verifica_company_api_token(self):
        dados = self.serializer_company.data
        self.assertEqual(dados['api_token'], self.company.api_token)

    def test_verifica_company_id(self):
        dados = self.serializer_company.data
        self.assertEqual(dados['id'], self.company.id)


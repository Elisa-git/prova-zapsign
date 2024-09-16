from django.test import TestCase
from Zapi.models import Company
from Zapi.serializers import CompanySerializer

class SerializerCompanyTestCase:
    
    def setUp(self):
        self.company = Company(
            name = 'Empresa company'
        )

        self.serializer_company = CompanySerializer(isinstance=self.company)

    def test_verifica_campos_serializados_company(self):
        dados = self.serializer_company.data
        self.assertEqual()
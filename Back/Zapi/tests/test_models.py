from django.test import TestCase
from Zapi.models import Company
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


# class ModelDocumentTestCase(TestCase):
# class ModelSignerTestCase(TestCase):

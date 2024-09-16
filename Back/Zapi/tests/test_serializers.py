from django.test import TestCase
from Zapi.models import Company, Document,Signer
from Zapi.serializers import CompanySerializer, DocumentSerializer, SignerSerializer, ListaDocumentosDaEmpresaSerializer, GetSignersFromDocument
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

class SerializerDocumentTestCase(TestCase):
    
    def setUp(self):
        self.company = Company (
            name = 'Empresa company'
        )

        self.document = Document(
            name = 'Documento Um',
            status = 'Novo',
            created_by = 'Fulano de Tal',
            companyId = self.company,
            openId = 123
        )

        self.serializer_document = DocumentSerializer(instance=self.document)

    def test_verifica_conteudo_campos_serializados_document(self):
        dados = self.serializer_document.data
        self.assertSetEqual(set(dados.keys()), set(['id', 'name', 'status', 'created_at', 'last_updated_at', 'created_by', 'company']))

    def test_verifica_conteudo_campos_serializados_documents(self):
        dados = self.serializer_document.data

        self.assertEqual(dados['id'], self.document.id)
        self.assertEqual(dados['name'], self.document.name)
        self.assertEqual(dados['status'], self.document.status)
        self.assertEqual(dados['created_at'], self.document.created_at)
        self.assertEqual(dados['last_updated_at'], self.document.last_updated_at)
        self.assertEqual(dados['created_by'], self.document.created_by)
        self.assertEqual(dados['company'], self.document.companyId.name)

class SerializerSignerTestCase(TestCase):

    def setUp(self):
        self.company = Company (
            name = 'Empresa company'
        )

        self.document = Document(
            name = 'Documento Um',
            status = 'Novo',
            created_by = 'Fulano de Tal',
            companyId = self.company,
            openId = 123
        )

        self.signer = Signer (
            token = '123',
            status = 'Novo',
            name = 'Fulano',
            email = 'fula@email.com',
            externalId = settings.API_TOKEN,
            documentId = self.document
        )

        self.serializer_signer = SignerSerializer(instance=self.signer)
    
    def test_verifica_conteudo_campos_serializados_signer(self):
        dados = self.serializer_signer.data
        self.assertSetEqual(set(dados.keys()), set(['id', 'token', 'status', 'name', 'email', 'externalId', 'documentId']))

    def test_verifica_conteudo_campos_serializados_signers(self):
        dados = self.serializer_signer.data
        self.assertEqual(dados['id'], self.signer.id)
        self.assertEqual(dados['token'], self.signer.token)
        self.assertEqual(dados['status'], self.signer.status)
        self.assertEqual(dados['name'], self.signer.name)
        self.assertEqual(dados['email'], self.signer.email)
        self.assertEqual(dados['externalId'], self.signer.externalId)
        self.assertEqual(dados['documentId'], self.signer.documentId.id)

class SerializerListaDocumentosDaEmpresaTestCase(TestCase):

    def setUp(self):
        self.company = Company (
            name = 'Empresa company'
        )

        self.document = Document(
            name = 'Documento Um',
            status = 'Novo',
            created_by = 'Fulano de Tal',
            companyId = self.company,
            openId = 123
        )

        self.documents_company = ListaDocumentosDaEmpresaSerializer(instance=self.document)

    def test_verifica_campos_serializados_documentos_empresa(self):
        dados = self.documents_company.data
        self.assertSetEqual(set(dados.keys()), set(['name', 'companyId']))

    def test_verifica_campos_serializados_documentos_empresa(self):
        dados = self.documents_company.data
        self.assertEqual(dados['name'], self.document.name)
        self.assertEqual(dados['companyId'], self.document.companyId.name)

class SerializerGetSignersFromDocumentTestCase(TestCase):

    def setUp(self):
        self.company = Company (
            name = 'Empresa company'
        )

        self.document = Document(
            name = 'Documento Um',
            status = 'Novo',
            created_by = 'Fulano de Tal',
            companyId = self.company,
            openId = 123
        )

        self.signer = Signer (
            token = '123',
            status = 'Novo',
            name = 'Fulano',
            email = 'fula@email.com',
            externalId = settings.API_TOKEN,
            documentId = self.document
        )

        self.signers_document = SignerSerializer(instance=self.signer)

    def test_verifica_campos_serializados_signatarios_documento(self):
        dados = self.signers_document.data
        self.assertSetEqual(set(dados.keys()), set(['id', 'name', 'email', 'documentId']))

    def test_verifica_campos_serializados_signatarios_documento(self):
        dados = self.signers_document.data
        self.assertEqual(dados['id'], self.signer.id)
        self.assertEqual(dados['name'], self.signer.name)
        self.assertEqual(dados['email'], self.signer.email)
        self.assertEqual(dados['documentId'], self.signer.documentId.id)

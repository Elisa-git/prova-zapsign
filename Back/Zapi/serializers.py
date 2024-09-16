from rest_framework import serializers
from Zapi.models import Company, Document, Signer

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'
        
class DocumentSerializer(serializers.ModelSerializer):
    company = serializers.ReadOnlyField(source='companyId.name')

    class Meta:
        model = Document
        fields = ['id', 'name', 'status', 'created_at', 'last_updated_at', 'created_by', 'company']
    
    def get_empresa(self, obj):
        return obj.get_empresa_display()

class SignerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signer
        fields = '__all__'

class ListaDocumentosDaEmpresaSerializer(serializers.ModelSerializer):
    companyId = serializers.ReadOnlyField(source='companyId.name')
    class Meta:
        model = Document
        fields = ['name', 'companyId']

class GetSignersFromDocument(serializers.ModelSerializer):
    documentId = serializers.ReadOnlyField(source='documentId.name')
    class Meta:
        model = Signer
        fields = ['id', 'name', 'email', 'documentId']
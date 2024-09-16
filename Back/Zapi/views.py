from Zapi.models import Company, Document, Signer
from Zapi.serializers import CompanySerializer, DocumentSerializer, SignerSerializer, ListaDocumentosDaEmpresaSerializer, GetSignersFromDocument
from rest_framework import viewsets, generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
from django.db import transaction
import requests
import traceback

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

class SignerViewSet(viewsets.ModelViewSet):
    queryset = Signer.objects.all()
    serializer_class = SignerSerializer

class ListaDocumentosDaEmpresa(generics.ListAPIView):
    def get_queryset(self):
        queryset = Document.objects.filter(companyId=self.kwargs['pk'])
        return queryset
    serializer_class = ListaDocumentosDaEmpresaSerializer

class SignersFromDocument(generics.ListAPIView):
    
    def get_queryset(self):
        queryset = Signer.objects.filter(documentId=self.kwargs['pk'])
        return queryset
    serializer_class = GetSignersFromDocument

class ItemCreateView(APIView):
        
    def post_Document(self, document):
        try:
            if not Company.objects.exists():                
                Company.objects.create(name='Primeira Empresa')

            company = Company.objects.filter(id=1).first()
            print(f"CREAT: {company}")
            print(f"OPEN ID: {document.get('open_id')}")

            documentRequest = Document.objects.create(
                name = document.get('name'),
                created_by = document["created_by"]["email"],
                companyId = company,
                openId = document.get('open_id'),
                token = document.get('token'),
                status = document.get('status')
            )
            print(f"DOCUMENT: {documentRequest}")
            

            return documentRequest
        except Exception as exception:
            print(f"Erro ao criar o documento: {str(exception)}")
            print(f'TRACE: {traceback.format_exc()}')
            raise exception

    def post_Signers(self, signer, document):
        print(f"CHEGUEI")

        signatarios = signer.get('signers', [])

        signer_list = [

            Signer(
                name = signatario['name'],
                email = signatario['email'],
                documentId = document,
                status = signatario['status'],
                token = signatario['token']
            )
            for signatario in signatarios
        ]

        try:
            Signer.objects.bulk_create(signer_list)
            print(f"Signatários criados em massa: {signer_list}")
        except Exception as exception:
            print(f"Erro ao criar signatários: {str(exception)}")
            raise exception

    def post(self, request):
        print(f'RECEBENDO: {request.data}')

        signers_list = []
        signatarios = request.data.get('signatarios', [])
        url_pdf = 'https://drive.google.com/file/d/1WOm8LZnTgQNGcQOXZvYxrcEOneYjHD1r/view?usp=sharing' 

        for signatario in signatarios:
            signer = {
                "name": signatario['name'],
                "email": signatario['email'],
            }

            signers_list.append(signer)

        request_externo = {
            "name": request.data.get('name'),
            "url_pdf": url_pdf,
            "signers": signers_list,
            "created_by": request.data.get('created_by'),
        }

        header = {
            "Authorization": f"Bearer {settings.API_TOKEN}"
        }

        print(f'TESTE: { request_externo }')
        print(f'HEADER: { header }')

        try:
            with transaction.atomic():
                # response_externo = requests.post(settings.API_ZAP_SIGN, json=request_externo, headers=header)
                
                response_externo = {
                    "sandbox": False,
                    "external_id": "",
                    "open_id": 2,
                    "token": "7b943a78-9ba4-4878-aa18-b56562646588",
                    "name": "testeNOVO33.pdf",
                    "folder_path": "/",
                    "status": "pending",
                    "rejected_reason": None,
                    "lang": "pt-br",
                    "original_file": "https://zapsign.s3.amazonaws.com/sandbox/dev/2024/9/api/df7a3740-5f27-4bad-88a7-bb3936619420.pdf?AWSAccessKeyId=AKIASUFZJ7JCTI2ZRGWX&Signature=BDIScazkj34e1B7e1Ni%2FSNd75yU%3D&Expires=1726326942",
                    "signed_file": None,
                    "extra_docs": [],
                    "created_through": "api",
                    "deleted": False,
                    "deleted_at": None,
                    "signed_file_only_finished": False,
                    "disable_signer_emails": False,
                    "brand_logo": "",
                    "brand_primary_color": "",
                    "created_at": "2024-09-14T14:15:42.562305Z",
                    "last_update_at": "2024-09-14T14:15:42.562323Z",
                    "created_by": {
                        "email": "Elisa Mesquita"
                    },
                    "template": None,
                    "signers": [
                        {
                            "external_id": "",
                            "sign_url": "https://sandbox.app.zapsign.com.br/verificar/2b1f37f2-59e1-48c9-8ca6-c9fd1adad793",
                            "token": "2b1f37f2-59e1-48c9-8ca6-c9fd1adad793",
                            "status": "new",
                            "name": "Christopher D R",
                            "lock_name": False,
                            "email": "sig344@natario.com",
                            "lock_email": False,
                            "hide_email": False,
                            "blank_email": False,
                            "phone_country": "55",
                            "phone_number": "",
                            "lock_phone": False,
                            "hide_phone": False,
                            "blank_phone": False,
                            "times_viewed": 0,
                            "last_view_at": None,
                            "signed_at": None,
                            "auth_mode": "assinaturaTela",
                            "qualification": "",
                            "require_selfie_photo": False,
                            "require_document_photo": False,
                            "geo_latitude": None,
                            "geo_longitude": None,
                            "redirect_link": "",
                            "signature_image": None,
                            "visto_image": None,
                            "document_photo_url": "",
                            "document_verse_photo_url": "",
                            "selfie_photo_url": "",
                            "selfie_photo_url2": ""
                        }
                    ],
                    "answers": [],
                    "auto_reminder": 0,
                    "signature_report": None,
                    "tsa_country": None,
                    "use_timestamp": True
                }

                # if response_externo.status_code != 200:
                #     return Response({"message": "Falha ao se comunicar com API externa"}, status=response_externo.status_code)

                document = self.post_Document(response_externo)
                print(f"CHEGUEI1 {document}")
                if len(signers_list) > 0 :
                    self.post_Signers(response_externo, document)

            return Response({"message": "Documento e signatários criados com sucesso"}, status=status.HTTP_201_CREATED)

        except requests.exceptions.RequestException as exception:
            return Response({"message": f"Erro no processo: {str(exception)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as exception:
            return Response({"message": f"Erro ao criar documento ou signatários: {str(exception)}"}, status=status.HTTP_400_BAD_REQUEST)

class ItemUpdateView(APIView):

    def patch_Document(self, document):
        try:
            response_Documento = Document.objects.filter(id=document.get('id')).update(**document)
            return response_Documento
        except Exception as exception:
            print(f"Erro ao editar o documento: {str(exception)}")
            raise exception

    def patch_Signers(self, signers, id_document):
        document = Document.objects.get(id=id_document)

        for signatario in signers:
            try:
                signatario['documentId'] = document
                Signer.objects.update_or_create(id = signatario['id'], defaults = signatario)

            except Exception as exception:
                print(f"Erro ao editar o signatario: {str(exception)}")
                raise exception
            
    def delete_Signers(self, signers):
        for signatario in signers:
            try:
                signer = Signer.objects.get(id=signatario['id'])
                signer.delete()

            except Exception as exception:
                print(f"Erro ao excluir o signatario: {str(exception)}")
                raise exception

    def patch(self, request):
        
        documento = request.data
        signatarios = documento.get('signatarios', [])
        signatariosRemovidos = documento.get('signatariosRemovidos', [])
        documento.pop('signatarios', None)
        documento.pop('signatariosRemovidos', None)
        print(f'SIG:{signatarios}')
        print(f'DOC:{documento}')
        print(f'SIG REMOV:{signatariosRemovidos}')

        try:
            with transaction.atomic():
                self.patch_Document(documento)
                if len(signatarios) > 0:
                    self.patch_Signers(signatarios, documento.get('id'))
                if len(signatariosRemovidos) > 0:
                    self.delete_Signers(signatariosRemovidos)

            return Response({"message": "Documento editado com sucesso"}, status=status.HTTP_201_CREATED)
        
        except requests.exceptions.RequestException as exception:
            return Response({"message": f"Erro no processo: {str(exception)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
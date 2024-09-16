from django.contrib import admin
from django.urls import path, include
from Zapi.views import CompanyViewSet, DocumentViewSet, SignerViewSet, ListaDocumentosDaEmpresa, ItemCreateView, SignersFromDocument, ItemUpdateView
from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=False)
router.register('companies', CompanyViewSet, basename='Companies')
router.register('documents', DocumentViewSet, basename='Documents')
router.register('signers', SignerViewSet, basename='Signers')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('document/<int:pk>/companies/', ListaDocumentosDaEmpresa.as_view()),
    path('document/<int:pk>/signers/', SignersFromDocument.as_view()),
    path('document/create/', ItemCreateView.as_view(), name='create-document'),
    path('signers/update/', ItemUpdateView.as_view(), name='update-signers'),
]

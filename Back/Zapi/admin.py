from django.contrib import admin
from Zapi.models import Company, Document, Signer

class Companies(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'last_updated_at', 'api_token',)
    list_display_links = ('id', 'name',)

admin.site.register(Company, Companies)

class Documents(admin.ModelAdmin):
    list_display = ('id', 'openId', 'name', 'token', 'status', 'created_at', 'last_updated_at', 'created_by', 'externalId', 'companyId',)
    list_display_links = ('id', 'name',)
    list_per_page = 10
    search_fields = ("name",)

admin.site.register(Document, Documents)

class Signers(admin.ModelAdmin):
    list_display = ('id', 'token', 'status', 'name',  'email', 'externalId', 'documentId',)
    list_display_links = ('id', 'name',)

admin.site.register(Signer, Signers)
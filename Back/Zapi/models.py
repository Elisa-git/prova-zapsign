from django.db import models
from django.conf import settings

class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)
    api_token = models.CharField(max_length=255, null=False, blank=True)

    def save(self, *args, **kwargs):
        self.api_token = settings.API_TOKEN
        super().save(*args, **kwargs)

class Document(models.Model):

    id = models.AutoField(primary_key=True)
    openId = models.IntegerField(null=False, blank=True)
    token = models.CharField(max_length=255, null=False, blank=True)
    name = models.CharField(max_length=255, null=False)
    status = models.CharField(max_length=50, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=255, null=False)
    externalId = models.CharField(max_length=255, null=False, blank=True)
    companyId = models.ForeignKey(Company, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.externalId = settings.API_TOKEN
        super().save(*args, **kwargs)

class Signer(models.Model):
    id = models.AutoField(primary_key=True)
    token = models.CharField(max_length=255, null=False, blank=True)
    status = models.CharField(max_length=255, null=False)
    name = models.CharField(max_length=255, null=False)
    email = models.EmailField(max_length=255, null=False)
    externalId = models.CharField(max_length=255, null=False, blank=True)
    documentId = models.ForeignKey(Document, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.externalId = settings.API_TOKEN
        super().save(*args, **kwargs)
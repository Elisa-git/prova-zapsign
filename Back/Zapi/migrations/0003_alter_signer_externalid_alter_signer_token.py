# Generated by Django 5.1.1 on 2024-09-13 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Zapi', '0002_alter_document_externalid_alter_document_openid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signer',
            name='externalId',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='signer',
            name='token',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]

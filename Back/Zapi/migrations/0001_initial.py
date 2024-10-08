# Generated by Django 5.1.1 on 2024-09-13 18:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_updated_at', models.DateTimeField(auto_now=True)),
                ('api_token', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('openId', models.IntegerField()),
                ('token', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('I', 'Iniciado'), ('E', 'Encerrado')], max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(max_length=255)),
                ('externalId', models.CharField(max_length=255)),
                ('companyId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Zapi.company')),
            ],
        ),
        migrations.CreateModel(
            name='Signer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('token', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('S', 'Assinou'), ('N', 'Aguardando Assiantura')], max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('externalId', models.CharField(max_length=255)),
                ('documentId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Zapi.document')),
            ],
        ),
    ]

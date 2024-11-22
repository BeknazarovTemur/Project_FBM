# Generated by Django 5.1.3 on 2024-11-21 11:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0007_document_body_af_document_body_ar_and_more'),
        ('languages', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='document',
            options={},
        ),
        migrations.AddField(
            model_name='document',
            name='language',
            field=models.ForeignKey(default='', limit_choices_to={'is_active': True}, on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='languages.language', verbose_name='Language'),
        ),
    ]

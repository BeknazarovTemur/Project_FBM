# Generated by Django 5.1.3 on 2024-11-13 11:04

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0003_document_body_delete_filecategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='body_en',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_ru',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_uz',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_en',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_ru',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_uz',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='document',
            name='body',
            field=ckeditor.fields.RichTextField(default='', verbose_name='body'),
        ),
        migrations.AlterField(
            model_name='document',
            name='title',
            field=models.CharField(max_length=50, verbose_name='title'),
        ),
    ]

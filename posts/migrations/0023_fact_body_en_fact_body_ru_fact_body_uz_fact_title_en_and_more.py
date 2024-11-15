# Generated by Django 5.1.3 on 2024-11-13 11:04

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0022_call_federation_content_en_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='fact',
            name='body_en',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='fact',
            name='body_ru',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='fact',
            name='body_uz',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='fact',
            name='title_en',
            field=models.CharField(max_length=100, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='fact',
            name='title_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='fact',
            name='title_uz',
            field=models.CharField(max_length=100, null=True, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='call',
            name='short_content',
            field=ckeditor.fields.RichTextField(verbose_name='short_content'),
        ),
        migrations.AlterField(
            model_name='call',
            name='short_content_en',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='short_content'),
        ),
        migrations.AlterField(
            model_name='call',
            name='short_content_ru',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='short_content'),
        ),
        migrations.AlterField(
            model_name='call',
            name='short_content_uz',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='short_content'),
        ),
        migrations.AlterField(
            model_name='fact',
            name='body',
            field=ckeditor.fields.RichTextField(verbose_name='body'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='content'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content_en',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='content'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content_ru',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='content'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content_uz',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='content'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='body',
            field=ckeditor.fields.RichTextField(verbose_name='body'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='body_en',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='body'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='body_ru',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='body'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='body_uz',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='body'),
        ),
    ]
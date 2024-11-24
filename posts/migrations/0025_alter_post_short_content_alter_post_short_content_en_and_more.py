# Generated by Django 5.1.3 on 2024-11-13 11:45

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0024_alter_post_short_content_alter_post_short_content_en_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='short_content',
            field=ckeditor.fields.RichTextField(blank=True, max_length=300, verbose_name='short_content'),
        ),
        migrations.AlterField(
            model_name='post',
            name='short_content_en',
            field=ckeditor.fields.RichTextField(blank=True, max_length=300, null=True, verbose_name='short_content'),
        ),
        migrations.AlterField(
            model_name='post',
            name='short_content_ru',
            field=ckeditor.fields.RichTextField(blank=True, max_length=300, null=True, verbose_name='short_content'),
        ),
        migrations.AlterField(
            model_name='post',
            name='short_content_uz',
            field=ckeditor.fields.RichTextField(blank=True, max_length=300, null=True, verbose_name='short_content'),
        ),
    ]

# Generated by Django 5.1.3 on 2024-11-20 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0005_alter_document_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Is Active'),
        ),
    ]
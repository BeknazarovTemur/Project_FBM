# Generated by Django 5.1.3 on 2024-11-21 05:55

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='uuid')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Catalog Name')),
            ],
            options={
                'verbose_name': 'Catalog',
                'verbose_name_plural': 'Catalogs',
                'db_table': 'language_catalogs',
                'ordering': ['-created_time'],
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='uuid')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Language Name')),
                ('code', models.CharField(max_length=10, unique=True, verbose_name='Language Code')),
                ('is_active', models.BooleanField(default=False, verbose_name='Is Active')),
            ],
            options={
                'verbose_name': 'Language',
                'verbose_name_plural': 'Languages',
                'db_table': 'languages',
                'ordering': ['-created_time'],
            },
        ),
        migrations.CreateModel(
            name='OriginalWord',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='uuid')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('original_word', models.TextField(unique=True, verbose_name='Original Word')),
                ('catalog', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='original_words', to='languages.catalog', verbose_name='Catalog')),
            ],
            options={
                'verbose_name': 'Original Word',
                'verbose_name_plural': 'Original Words',
                'db_table': 'original_words',
                'ordering': ['-created_time'],
            },
        ),
        migrations.CreateModel(
            name='Translations',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='uuid')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('translation_text', models.CharField(max_length=255, verbose_name='Translation Text')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='languages.language', verbose_name='Language')),
                ('original_word', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='languages.originalword', verbose_name='Original Word')),
            ],
            options={
                'verbose_name': 'Translation',
                'verbose_name_plural': 'Translations',
                'db_table': 'translations',
                'ordering': ['-created_time'],
            },
        ),
    ]
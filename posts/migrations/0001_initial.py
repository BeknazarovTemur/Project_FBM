# Generated by Django 5.1.3 on 2024-11-28 06:16

import ckeditor.fields
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('languages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Call',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head', models.CharField(max_length=100, verbose_name='head')),
                ('short_content', ckeditor.fields.RichTextField(verbose_name='short_content')),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('federation_content', models.CharField(default='', max_length=200, verbose_name='federation_content')),
                ('federation_number', models.CharField(max_length=100, verbose_name='federation_number')),
                ('state_content', models.CharField(max_length=200, verbose_name='state_content')),
                ('state_number', models.CharField(max_length=100, verbose_name='state_number')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
            ],
            options={
                'verbose_name': 'Call',
                'verbose_name_plural': 'Calls',
            },
        ),
        migrations.CreateModel(
            name='Fact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('body', ckeditor.fields.RichTextField(verbose_name='body')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
            ],
            options={
                'verbose_name': 'Fact',
                'verbose_name_plural': 'Facts',
            },
        ),
        migrations.CreateModel(
            name='Helpline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head', models.CharField(default='', max_length=200, verbose_name='head')),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('federation_title', models.CharField(default='', max_length=200, verbose_name='federation_title')),
                ('federation_number', models.CharField(max_length=100, verbose_name='federation_number')),
                ('state_title', models.CharField(default='', max_length=200, verbose_name='state_title')),
                ('state_number', models.CharField(max_length=100, verbose_name='state_number')),
                ('tag', models.CharField(default='', max_length=200, verbose_name='tag')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
            ],
            options={
                'verbose_name': 'Helpline',
                'verbose_name_plural': 'Helplines',
            },
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
            ],
            options={
                'verbose_name': 'Link',
                'verbose_name_plural': 'Links',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('url', models.URLField(blank=True, null=True, verbose_name='URL')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
            ],
            options={
                'verbose_name': 'Menu',
                'verbose_name_plural': 'Menus',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('short_content', ckeditor.fields.RichTextField(blank=True, max_length=300, verbose_name='short_content')),
                ('content', ckeditor.fields.RichTextField(verbose_name='content')),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
            ],
            options={
                'verbose_name': 'Slider',
                'verbose_name_plural': 'Sliders',
            },
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100, verbose_name='Name')),
                ('url', models.URLField(blank=True, null=True, verbose_name='URL')),
                ('is_active', models.BooleanField(default=True)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='posts.menu')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='posts.menuitem')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='SliderTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', ckeditor.fields.RichTextField()),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='languages.language')),
                ('slider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='posts.slider')),
            ],
            options={
                'verbose_name': 'Slider Translation',
                'verbose_name_plural': 'Slider Translations',
                'unique_together': {('slider', 'language')},
            },
        ),
    ]

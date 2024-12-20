# Generated by Django 5.1.3 on 2024-11-28 06:57

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('languages', '0001_initial'),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menuitem',
            options={'ordering': ['id'], 'verbose_name': 'MenuItem', 'verbose_name_plural': 'MenuItems'},
        ),
        migrations.RemoveField(
            model_name='post',
            name='content',
        ),
        migrations.RemoveField(
            model_name='post',
            name='short_content',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
        migrations.CreateModel(
            name='PostTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('short_content', ckeditor.fields.RichTextField(blank=True, max_length=300, verbose_name='short_content')),
                ('content', ckeditor.fields.RichTextField(verbose_name='content')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='languages.language')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='posts.post')),
            ],
            options={
                'verbose_name': 'Post Translation',
                'verbose_name_plural': 'Post Translations',
                'unique_together': {('post', 'language')},
            },
        ),
    ]

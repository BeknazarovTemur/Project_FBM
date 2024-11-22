# Generated by Django 5.1.3 on 2024-11-19 06:00

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0009_createquestion_rename_add_time_question_created_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='question',
        ),
        migrations.DeleteModel(
            name='CreateQuestion',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='created_at',
            new_name='add_time',
        ),
        migrations.RemoveField(
            model_name='question',
            name='body',
        ),
        migrations.AddField(
            model_name='question',
            name='detail',
            field=ckeditor.fields.RichTextField(default='', verbose_name='detail'),
        ),
        migrations.AddField(
            model_name='question',
            name='number',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='title',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
    ]

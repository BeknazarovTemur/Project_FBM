# Generated by Django 5.1.3 on 2024-11-19 06:07

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0010_remove_answer_question_delete_createquestion_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_body', ckeditor.fields.RichTextField(verbose_name='question body')),
                ('answer_body', ckeditor.fields.RichTextField(verbose_name='answer body')),
                ('add_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

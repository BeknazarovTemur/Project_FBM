# Generated by Django 5.1.3 on 2024-11-19 05:26

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0006_alter_question_options_alter_question_title_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='detail',
        ),
        migrations.RemoveField(
            model_name='question',
            name='detail_en',
        ),
        migrations.RemoveField(
            model_name='question',
            name='detail_ru',
        ),
        migrations.RemoveField(
            model_name='question',
            name='detail_uz',
        ),
        migrations.RemoveField(
            model_name='question',
            name='number',
        ),
        migrations.RemoveField(
            model_name='question',
            name='title',
        ),
        migrations.RemoveField(
            model_name='question',
            name='title_en',
        ),
        migrations.RemoveField(
            model_name='question',
            name='title_ru',
        ),
        migrations.RemoveField(
            model_name='question',
            name='title_uz',
        ),
        migrations.AddField(
            model_name='question',
            name='content',
            field=ckeditor.fields.RichTextField(default='', verbose_name='content'),
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', ckeditor.fields.RichTextField(verbose_name='Content')),
                ('is_approved', models.BooleanField(default=False, verbose_name='Is Approved')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='Added Time')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='question.question', verbose_name='Question')),
            ],
            options={
                'verbose_name': 'Answer',
                'verbose_name_plural': 'Answers',
                'ordering': ['-add_time'],
            },
        ),
    ]
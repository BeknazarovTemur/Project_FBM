# Generated by Django 5.1.3 on 2024-11-15 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0005_alter_question_detail_alter_question_detail_en_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': 'Question', 'verbose_name_plural': 'Questions'},
        ),
        migrations.AlterField(
            model_name='question',
            name='title',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='question',
            name='title_en',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='title_ru',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='title_uz',
            field=models.CharField(max_length=300, null=True),
        ),
    ]

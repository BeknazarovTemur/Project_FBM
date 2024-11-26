# Generated by Django 5.1.3 on 2024-11-13 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0019_alter_menu_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='name_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='menu',
            name='name_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='menu',
            name='name_uz',
            field=models.CharField(max_length=100, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='menu',
            name='url_en',
            field=models.URLField(blank=True, null=True, verbose_name='Url'),
        ),
        migrations.AddField(
            model_name='menu',
            name='url_ru',
            field=models.URLField(blank=True, null=True, verbose_name='Url'),
        ),
        migrations.AddField(
            model_name='menu',
            name='url_uz',
            field=models.URLField(blank=True, null=True, verbose_name='Url'),
        ),
    ]

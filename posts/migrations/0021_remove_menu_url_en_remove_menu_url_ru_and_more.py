# Generated by Django 5.1.3 on 2024-11-13 07:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0020_menu_name_en_menu_name_ru_menu_name_uz_menu_url_en_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='url_en',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='url_ru',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='url_uz',
        ),
        migrations.AddField(
            model_name='menuitem',
            name='name_en',
            field=models.CharField(default='', max_length=100, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='name_ru',
            field=models.CharField(default='', max_length=100, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='name_uz',
            field=models.CharField(default='', max_length=100, null=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='url',
            field=models.URLField(blank=True, null=True, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='posts.menu'),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='name',
            field=models.CharField(default='', max_length=100, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='url',
            field=models.URLField(blank=True, null=True, verbose_name='URL'),
        ),
    ]

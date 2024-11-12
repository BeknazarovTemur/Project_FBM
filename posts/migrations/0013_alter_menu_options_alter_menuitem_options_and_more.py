# Generated by Django 5.1.3 on 2024-11-12 06:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0012_alter_menu_options_menu_is_active_menu_url_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menu',
            options={},
        ),
        migrations.AlterModelOptions(
            name='menuitem',
            options={'ordering': ['id']},
        ),
        migrations.RemoveField(
            model_name='menu',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='url',
        ),
        migrations.AddField(
            model_name='menuitem',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='posts.menuitem'),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='menu',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='items', to='posts.menu'),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
    ]

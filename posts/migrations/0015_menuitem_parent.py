# Generated by Django 5.1.3 on 2024-11-12 06:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0014_remove_menuitem_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='posts.menuitem'),
        ),
    ]

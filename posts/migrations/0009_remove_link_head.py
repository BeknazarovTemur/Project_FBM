# Generated by Django 5.1.3 on 2024-11-11 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_link_head'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='link',
            name='head',
        ),
    ]

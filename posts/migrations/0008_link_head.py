# Generated by Django 5.1.3 on 2024-11-11 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_helpline_head'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='head',
            field=models.CharField(default='', max_length=200),
        ),
    ]

# Generated by Django 5.1.3 on 2024-11-11 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_helpline_federation_title_helpline_state_title_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='helpline',
            name='head',
            field=models.CharField(default='', max_length=200),
        ),
    ]

# Generated by Django 5.1.3 on 2024-11-15 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appeal', '0004_alter_appeal_message'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appeal',
            options={'verbose_name': 'Appeal', 'verbose_name_plural': 'Appeals'},
        ),
    ]
# Generated by Django 5.1.3 on 2024-11-13 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0017_call'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Name'),
        ),
    ]
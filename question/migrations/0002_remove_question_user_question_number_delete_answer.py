# Generated by Django 5.1.3 on 2024-11-06 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='user',
        ),
        migrations.AddField(
            model_name='question',
            name='number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
    ]

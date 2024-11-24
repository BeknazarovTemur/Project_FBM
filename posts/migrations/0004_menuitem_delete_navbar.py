# Generated by Django 5.1.3 on 2024-11-11 06:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_alter_slider_body'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=200)),
                ('is_active', models.BooleanField(default=False)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='submenus', to='posts.menuitem')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.DeleteModel(
            name='Navbar',
        ),
    ]

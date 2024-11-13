# Generated by Django 5.1.3 on 2024-11-13 09:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0021_remove_menu_url_en_remove_menu_url_ru_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='call',
            name='federation_content_en',
            field=models.CharField(default='', max_length=200, null=True, verbose_name='federation_content'),
        ),
        migrations.AddField(
            model_name='call',
            name='federation_content_ru',
            field=models.CharField(default='', max_length=200, null=True, verbose_name='federation_content'),
        ),
        migrations.AddField(
            model_name='call',
            name='federation_content_uz',
            field=models.CharField(default='', max_length=200, null=True, verbose_name='federation_content'),
        ),
        migrations.AddField(
            model_name='call',
            name='head_en',
            field=models.CharField(max_length=100, null=True, verbose_name='head'),
        ),
        migrations.AddField(
            model_name='call',
            name='head_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='head'),
        ),
        migrations.AddField(
            model_name='call',
            name='head_uz',
            field=models.CharField(max_length=100, null=True, verbose_name='head'),
        ),
        migrations.AddField(
            model_name='call',
            name='short_content_en',
            field=models.TextField(null=True, verbose_name='short_content'),
        ),
        migrations.AddField(
            model_name='call',
            name='short_content_ru',
            field=models.TextField(null=True, verbose_name='short_content'),
        ),
        migrations.AddField(
            model_name='call',
            name='short_content_uz',
            field=models.TextField(null=True, verbose_name='short_content'),
        ),
        migrations.AddField(
            model_name='call',
            name='state_content_en',
            field=models.CharField(max_length=200, null=True, verbose_name='state_content'),
        ),
        migrations.AddField(
            model_name='call',
            name='state_content_ru',
            field=models.CharField(max_length=200, null=True, verbose_name='state_content'),
        ),
        migrations.AddField(
            model_name='call',
            name='state_content_uz',
            field=models.CharField(max_length=200, null=True, verbose_name='state_content'),
        ),
        migrations.AddField(
            model_name='call',
            name='title_en',
            field=models.CharField(max_length=200, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='call',
            name='title_ru',
            field=models.CharField(max_length=200, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='call',
            name='title_uz',
            field=models.CharField(max_length=200, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='helpline',
            name='federation_title_en',
            field=models.CharField(default='', max_length=200, null=True, verbose_name='federation_title'),
        ),
        migrations.AddField(
            model_name='helpline',
            name='federation_title_ru',
            field=models.CharField(default='', max_length=200, null=True, verbose_name='federation_title'),
        ),
        migrations.AddField(
            model_name='helpline',
            name='federation_title_uz',
            field=models.CharField(default='', max_length=200, null=True, verbose_name='federation_title'),
        ),
        migrations.AddField(
            model_name='helpline',
            name='head_en',
            field=models.CharField(default='', max_length=200, null=True, verbose_name='head'),
        ),
        migrations.AddField(
            model_name='helpline',
            name='head_ru',
            field=models.CharField(default='', max_length=200, null=True, verbose_name='head'),
        ),
        migrations.AddField(
            model_name='helpline',
            name='head_uz',
            field=models.CharField(default='', max_length=200, null=True, verbose_name='head'),
        ),
        migrations.AddField(
            model_name='helpline',
            name='state_title_en',
            field=models.CharField(default='', max_length=200, null=True, verbose_name='state_title'),
        ),
        migrations.AddField(
            model_name='helpline',
            name='state_title_ru',
            field=models.CharField(default='', max_length=200, null=True, verbose_name='state_title'),
        ),
        migrations.AddField(
            model_name='helpline',
            name='state_title_uz',
            field=models.CharField(default='', max_length=200, null=True, verbose_name='state_title'),
        ),
        migrations.AddField(
            model_name='helpline',
            name='tag_en',
            field=models.CharField(default='', max_length=200, null=True, verbose_name='tag'),
        ),
        migrations.AddField(
            model_name='helpline',
            name='tag_ru',
            field=models.CharField(default='', max_length=200, null=True, verbose_name='tag'),
        ),
        migrations.AddField(
            model_name='helpline',
            name='tag_uz',
            field=models.CharField(default='', max_length=200, null=True, verbose_name='tag'),
        ),
        migrations.AddField(
            model_name='helpline',
            name='title_en',
            field=models.CharField(max_length=200, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='helpline',
            name='title_ru',
            field=models.CharField(max_length=200, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='helpline',
            name='title_uz',
            field=models.CharField(max_length=200, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='link',
            name='title_en',
            field=models.CharField(max_length=100, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='link',
            name='title_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='link',
            name='title_uz',
            field=models.CharField(max_length=100, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='post',
            name='content_en',
            field=models.TextField(null=True, verbose_name='content'),
        ),
        migrations.AddField(
            model_name='post',
            name='content_ru',
            field=models.TextField(null=True, verbose_name='content'),
        ),
        migrations.AddField(
            model_name='post',
            name='content_uz',
            field=models.TextField(null=True, verbose_name='content'),
        ),
        migrations.AddField(
            model_name='post',
            name='short_content_en',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='short_content'),
        ),
        migrations.AddField(
            model_name='post',
            name='short_content_ru',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='short_content'),
        ),
        migrations.AddField(
            model_name='post',
            name='short_content_uz',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='short_content'),
        ),
        migrations.AddField(
            model_name='post',
            name='title_en',
            field=models.CharField(max_length=100, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='post',
            name='title_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='post',
            name='title_uz',
            field=models.CharField(max_length=100, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='slider',
            name='body_en',
            field=models.TextField(null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='slider',
            name='body_ru',
            field=models.TextField(null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='slider',
            name='body_uz',
            field=models.TextField(null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='slider',
            name='title_en',
            field=models.CharField(max_length=100, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='slider',
            name='title_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='slider',
            name='title_uz',
            field=models.CharField(max_length=100, null=True, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='call',
            name='federation_content',
            field=models.CharField(default='', max_length=200, verbose_name='federation_content'),
        ),
        migrations.AlterField(
            model_name='call',
            name='federation_number',
            field=models.CharField(max_length=100, verbose_name='federation_number'),
        ),
        migrations.AlterField(
            model_name='call',
            name='head',
            field=models.CharField(max_length=100, verbose_name='head'),
        ),
        migrations.AlterField(
            model_name='call',
            name='short_content',
            field=models.TextField(verbose_name='short_content'),
        ),
        migrations.AlterField(
            model_name='call',
            name='state_content',
            field=models.CharField(max_length=200, verbose_name='state_content'),
        ),
        migrations.AlterField(
            model_name='call',
            name='state_number',
            field=models.CharField(max_length=100, verbose_name='state_number'),
        ),
        migrations.AlterField(
            model_name='call',
            name='title',
            field=models.CharField(max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='fact',
            name='body',
            field=models.TextField(verbose_name='body'),
        ),
        migrations.AlterField(
            model_name='fact',
            name='title',
            field=models.CharField(max_length=100, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='helpline',
            name='federation_number',
            field=models.CharField(max_length=100, verbose_name='federation_number'),
        ),
        migrations.AlterField(
            model_name='helpline',
            name='federation_title',
            field=models.CharField(default='', max_length=200, verbose_name='federation_title'),
        ),
        migrations.AlterField(
            model_name='helpline',
            name='head',
            field=models.CharField(default='', max_length=200, verbose_name='head'),
        ),
        migrations.AlterField(
            model_name='helpline',
            name='state_number',
            field=models.CharField(max_length=100, verbose_name='state_number'),
        ),
        migrations.AlterField(
            model_name='helpline',
            name='state_title',
            field=models.CharField(default='', max_length=200, verbose_name='state_title'),
        ),
        migrations.AlterField(
            model_name='helpline',
            name='tag',
            field=models.CharField(default='', max_length=200, verbose_name='tag'),
        ),
        migrations.AlterField(
            model_name='helpline',
            name='title',
            field=models.CharField(max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='link',
            name='title',
            field=models.CharField(max_length=100, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.category', verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(verbose_name='content'),
        ),
        migrations.AlterField(
            model_name='post',
            name='short_content',
            field=models.CharField(blank=True, max_length=200, verbose_name='short_content'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='body',
            field=models.TextField(verbose_name='body'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='title',
            field=models.CharField(max_length=100, verbose_name='title'),
        ),
    ]

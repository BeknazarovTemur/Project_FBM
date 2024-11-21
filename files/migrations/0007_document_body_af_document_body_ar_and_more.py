# Generated by Django 5.1.3 on 2024-11-21 07:46

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0006_document_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='body_af',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_ar',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_ar_dz',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_ast',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_az',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_be',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_bg',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_bn',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_br',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_bs',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_ca',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_ckb',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_cs',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_cy',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_da',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_de',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_dsb',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_el',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_en_au',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_en_gb',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_eo',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_es',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_es_ar',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_es_co',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_es_mx',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_es_ni',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_es_ve',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_et',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_eu',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_fa',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_fi',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_fr',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_fy',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_ga',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_gd',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_gl',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_he',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_hi',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_hr',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_hsb',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_hu',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_hy',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_ia',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_ig',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_ind',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_io',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_is',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_it',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_ja',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_ka',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_kab',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_kk',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_km',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_kn',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_ko',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_ky',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_lb',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_lt',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_lv',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_mk',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_ml',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_mn',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_mr',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_ms',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_my',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_nb',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_ne',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_nl',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_nn',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_os',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_pa',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_pl',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_pt',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_pt_br',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_ro',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_sk',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_sl',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_sq',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_sr',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_sr_latn',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_sv',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_sw',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_ta',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_te',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_tg',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_th',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_tk',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_tr',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_tt',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_udm',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_ug',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_uk',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_ur',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_vi',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_zh_hans',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='body_zh_hant',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_af',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_ar',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_ar_dz',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_ast',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_az',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_be',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_bg',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_bn',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_br',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_bs',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_ca',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_ckb',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_cs',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_cy',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_da',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_de',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_dsb',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_el',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_en_au',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_en_gb',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_eo',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_es',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_es_ar',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_es_co',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_es_mx',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_es_ni',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_es_ve',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_et',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_eu',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_fa',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_fi',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_fr',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_fy',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_ga',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_gd',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_gl',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_he',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_hi',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_hr',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_hsb',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_hu',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_hy',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_ia',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_ig',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_ind',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_io',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_is',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_it',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_ja',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_ka',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_kab',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_kk',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_km',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_kn',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_ko',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_ky',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_lb',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_lt',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_lv',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_mk',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_ml',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_mn',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_mr',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_ms',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_my',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_nb',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_ne',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_nl',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_nn',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_os',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_pa',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_pl',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_pt',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_pt_br',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_ro',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_sk',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_sl',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_sq',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_sr',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_sr_latn',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_sv',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_sw',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_ta',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_te',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_tg',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_th',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_tk',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_tr',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_tt',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_udm',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_ug',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_uk',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_ur',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_vi',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_zh_hans',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_zh_hant',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
    ]

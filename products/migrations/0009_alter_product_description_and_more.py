# Generated by Django 5.1.4 on 2024-12-24 16:58

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_privacypolicy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=ckeditor.fields.RichTextField(default='Default description'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='description_de',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='description_en',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]

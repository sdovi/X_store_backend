# Generated by Django 5.1.4 on 2024-12-24 17:09

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_alter_product_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='privacypolicy',
            name='content_de',
            field=ckeditor.fields.RichTextField(default='Sample text'),
            preserve_default=False,
        ),
    ]

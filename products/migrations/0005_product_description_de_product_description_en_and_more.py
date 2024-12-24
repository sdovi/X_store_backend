# Generated by Django 5.1.4 on 2024-12-18 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_banner_socialmedia'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description_de',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='description_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='name_de',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='name_en',
            field=models.CharField(max_length=255, null=True),
        ),
    ]

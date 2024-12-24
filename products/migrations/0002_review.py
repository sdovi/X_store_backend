# Generated by Django 5.1.4 on 2024-12-18 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='review_photos/', verbose_name='Фото')),
                ('text', models.TextField(verbose_name='Текст отзыва')),
                ('stars', models.IntegerField(default=0, verbose_name='Количество звезд')),
            ],
        ),
    ]
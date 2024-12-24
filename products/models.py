from django.db import models
from ckeditor.fields import RichTextField


class PrivacyPolicy(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()
    content_de = RichTextField()

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = RichTextField()
    image1 = models.ImageField(upload_to='products/', blank=True, null=True)
    image2 = models.ImageField(upload_to='products/', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='products')
    is_popular = models.BooleanField(default=False)

    in_home = models.BooleanField(default=True)

    def __str__(self):
        return self.name



class Review(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя")
    photo = models.ImageField(upload_to='review_photos/', blank=True, null=True, verbose_name="Фото")
    text = models.TextField(verbose_name="Текст отзыва")
    stars = models.IntegerField(verbose_name="Количество звезд", default=0)

    def __str__(self):
        return f'{self.name} - {self.stars} звезд'




class Banner(models.Model):
    image = models.ImageField(upload_to='banners/', verbose_name="Изображение баннера")

    def __str__(self):
        return f"Баннер {self.id}"
from django.db import models





class SocialMedia(models.Model):
    icon = models.FileField(upload_to='social_icons/', verbose_name="Иконка")
    text = models.CharField(max_length=255, verbose_name="Текст")
    link = models.TextField(verbose_name="Ссылка")

    def __str__(self):
        return self.text

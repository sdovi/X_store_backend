from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image1 = models.ImageField(upload_to='products/', blank=True, null=True)
    image2 = models.ImageField(upload_to='products/', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='products')
    is_popular = models.BooleanField(default=False)

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


class SocialMedia(models.Model):
    icon = models.ImageField(upload_to='social_icons/', verbose_name="Иконка")
    text = models.CharField(max_length=255, verbose_name="Текст")

    def __str__(self):
        return self.text
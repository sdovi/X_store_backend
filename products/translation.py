from modeltranslation.translator import register, TranslationOptions
from .models import Product  # Проверьте путь импорта

@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'description')  # Убедитесь, что эти поля существуют в модели

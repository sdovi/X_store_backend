from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Product, Category, Review, Banner, SocialMedia

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'image')


@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'icon', 'text')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):  # Здесь TranslationAdmin больше не используется
    list_display = ('id', 'name')


@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    list_display = ('id', 'name', 'price', 'in_stock', 'category')
    list_filter = ('category', 'in_stock')
    search_fields = ('name', 'description')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'stars', 'text', 'photo')
    list_filter = ('stars',)
    search_fields = ('name', 'text')

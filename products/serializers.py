from rest_framework import serializers
from .models import Product, Category, Review, Banner, SocialMedia, PrivacyPolicy


class PrivacyPolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivacyPolicy
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'description',
            'price',
            'in_stock',
            'category',
            'name_en',
            'name_de',
            'description_en',
            'description_de',
            "in_home",
            "is_popular",
            "image1",
            "image2"
        ]


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'


class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = '__all__'



class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'name', 'photo', 'text', 'stars']

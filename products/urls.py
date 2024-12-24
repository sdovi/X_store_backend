from django.urls import path, include
from .views import CategoryListCreateAPIView, ProductListCreateAPIView, ProductRetrieveUpdateDestroyAPIView,ReviewListCreateAPIView, ReviewRetrieveUpdateDestroyAPIView, BannerListCreateAPIView, BannerRetrieveUpdateDestroyAPIView, SocialMediaListCreateAPIView, SocialMediaRetrieveUpdateDestroyAPIView
from rest_framework.routers import DefaultRouter
from .views import PrivacyPolicyViewSet

router = DefaultRouter()
router.register(r'privacy-policies', PrivacyPolicyViewSet)

urlpatterns = [
    path('politika/', include(router.urls)),
    path('categories/', CategoryListCreateAPIView.as_view(), name='category-list-create'),
    path('products/', ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-detail'),

    path('reviews/', ReviewListCreateAPIView.as_view(), name='review-list-create'),
    path('reviews/<int:pk>/', ReviewRetrieveUpdateDestroyAPIView.as_view(), name='review-detail'),

    path('banners/', BannerListCreateAPIView.as_view(), name='banner-list-create'),
    path('banners/<int:pk>/', BannerRetrieveUpdateDestroyAPIView.as_view(), name='banner-detail'),
    path('social-media/', SocialMediaListCreateAPIView.as_view(), name='social-media-list-create'),
    path('social-media/<int:pk>/', SocialMediaRetrieveUpdateDestroyAPIView.as_view(), name='social-media-detail'),
]
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    SellerViewSet, 
    ClientViewSet, 
    ProductViewSet, 
    FriendshipViewSet, 
    OrderViewSet, 
    CategoryViewSet, 
    ReviewViewSet, 
    NotificationViewSet, 
    DeliveryViewSet, 
    WishlistViewSet
)

router = DefaultRouter()
router.register(r'sellers', SellerViewSet, basename='seller')
router.register(r'clients', ClientViewSet, basename='client')
router.register(r'products', ProductViewSet, basename='product')
router.register(r'friendships', FriendshipViewSet, basename='friendship')
router.register(r'orders', OrderViewSet, basename='order')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'reviews', ReviewViewSet, basename='review')
router.register(r'notifications', NotificationViewSet, basename='notification')
router.register(r'deliveries', DeliveryViewSet, basename='delivery')
router.register(r'wishlists', WishlistViewSet, basename='wishlist')

urlpatterns = [
    path('', include(router.urls)),  # Ajoute automatiquement les URL générées par le router
]

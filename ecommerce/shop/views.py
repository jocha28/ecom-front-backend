from rest_framework.viewsets import ModelViewSet
from .models import (
    Seller, 
    Product, 
    Friendship, 
    Client, 
    Order, 
    Category, 
    Review, 
    Notification, 
    Delivery,  
    Wishlist
)
from .serializers import (
    SellerSerializer, 
    ProductSerializer, 
    FriendshipSerializer, 
    ClientSerializer, 
    OrderSerializer, 
    CategorySerializer, 
    ReviewSerializer, 
    NotificationSerializer, 
    DeliverySerializer, 
    WishlistSerializer
)

# Vendeurs
class SellerViewSet(ModelViewSet):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer

# Clients
class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

# Produits
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# Amitiés
class FriendshipViewSet(ModelViewSet):
    queryset = Friendship.objects.all()
    serializer_class = FriendshipSerializer

# Commandes
class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

# Catégories
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# Avis
class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

# Notifications
class NotificationViewSet(ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

# Livraisons
class DeliveryViewSet(ModelViewSet):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer

# Listes de souhaits
class WishlistViewSet(ModelViewSet):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer

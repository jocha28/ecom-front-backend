from django.db import models
import os 
from django.core.exceptions import ObjectDoesNotExist

class Seller(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    whatsapp = models.CharField(max_length=100, blank=True, null=True)
    facebook = models.CharField(max_length=100, blank=True, null=True)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)  # Photo de profil
    cover_photo = models.ImageField(upload_to='cover_photos/', blank=True, null=True)  # Photo de couverture
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Sauvegarder l'instance originale si elle existe
        try:
            original = Seller.objects.get(pk=self.pk)
        except Seller.DoesNotExist:
            original = None

        # Vérifier si une nouvelle photo de profil est fournie
        if original:
            if not self.profile_picture and original.profile_picture:
                self.profile_picture = original.profile_picture
            if not self.cover_photo and original.cover_photo:
                self.cover_photo = original.cover_photo

        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Supprimer les fichiers associés en cas de suppression
        if self.profile_picture and os.path.isfile(self.profile_picture.path):
            os.remove(self.profile_picture.path)
        if self.cover_photo and os.path.isfile(self.cover_photo.path):
            os.remove(self.cover_photo.path)
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.name

    
class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    seller = models.ForeignKey('Seller', related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    min_price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Le prix minimum négociable")
    image = models.ImageField(upload_to='photo_images/', blank=True, null=True)
    video = models.FileField(upload_to='product_videos/', blank=True, null=True)
    product_whatsapp = models.CharField(max_length=100, blank=True, null=True)
    category = models.ForeignKey('Category', related_name='products', on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.seller.name}"

    def save(self, *args, **kwargs):
        try:
            original = Product.objects.get(pk=self.pk)
        except Product.DoesNotExist:
            original = None

        if original:
            # Si l'image n'a pas été modifiée, garder l'ancienne image
            if not self.image and original.image:
                self.image = original.image
            # Si la vidéo n'a pas été modifiée, garder l'ancienne vidéo
            if not self.video and original.video:
                self.video = original.video

        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Supprimer les fichiers associés si le produit est supprimé
        if self.image and os.path.isfile(self.image.path):
            os.remove(self.image.path)
        if self.video and os.path.isfile(self.video.path):
            os.remove(self.video.path)
        super().delete(*args, **kwargs)

class Friendship(models.Model):
    client = models.ForeignKey(Client, related_name='friendships', on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, related_name='friends', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['client', 'seller'], name='unique_friendship')
        ]

    def __str__(self):
        return f"{self.client.name} -> {self.seller.name}"

class Order(models.Model):
    client = models.ForeignKey(Client, related_name='orders', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='orders', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=50,
        choices=[
            ('pending', 'En attente'),
            ('confirmed', 'Confirmée'),
            ('shipped', 'Expédiée'),
            ('delivered', 'Livrée'),
            ('cancelled', 'Annulée'),
        ],
        default='pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Commande #{self.id} - {self.product.name} pour {self.client.name}"


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Review(models.Model):
    client = models.ForeignKey(Client, related_name='reviews', on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, related_name='reviews', on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE, blank=True, null=True)
    rating = models.PositiveIntegerField(default=1, choices=[(i, str(i)) for i in range(1, 6)])
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        target = self.product.name if self.product else self.seller.name
        return f"Avis de {self.client.name} sur {target}"

class Notification(models.Model):
    recipient = models.ForeignKey(Client, related_name='notifications', on_delete=models.CASCADE)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification pour {self.recipient.name}"

class Delivery(models.Model):
    order = models.OneToOneField(Order, related_name='delivery', on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    delivery_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    delivery_status = models.CharField(
        max_length=50,
        choices=[
            ('pending', 'En attente'),
            ('in_transit', 'En cours'),
            ('delivered', 'Livrée'),
        ],
        default='pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Livraison #{self.id} pour {self.order.id}"

class Wishlist(models.Model):
    client = models.ForeignKey(Client, related_name='wishlist', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='wishlists', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['client', 'product'], name='unique_wishlist_item')
        ]

    def __str__(self):
        return f"{self.client.name} souhaite {self.product.name}"

from django.db import models
from django.contrib.auth.models import AbstractUser, User

# Stores multiple clothes to trade for multiple clothes
class Trade(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="trader1")
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="trader2")



class Clothing(models.Model):
    # Tuple of choices for the type of clothing
    CLOTHING_TYPE_CHOICES = (
        ('Shirt', 'Shirt'),
        ('T-Shirt', 'T-Shirt'),
        ('Crop-Top', 'Crop-Top'),
        ('Jacket', 'Jacket'),
        ('Pant', 'Pant'),
        ('Sweater', 'Sweater'),
        ('Skirt', 'Skirt'),
        ('Jean', 'Jean'),
        ('Sweatpant', 'Sweatpant'),
        ('Legging', 'Legging'),
        ('Dress', 'Dress'),
        ('Suit', 'Suit'),
        ('Other', 'Other'),
    )
    # Tuple of choices of color
    COLOR_CHOICES = (
        ('Red', 'Red'),
        ('Orange', 'Orange'),
        ('Yellow', 'Yellow'),
        ('Green', 'Green'),
        ('Blue', 'Blue'),
        ('Purple', 'Purple'),
        ('Pink', 'Pink'),
        ('Brown', 'Brown'),
        ('Black', 'Black'),
        ('White', 'White'),
        ('Other', 'Other')
    )
    
    # Tuple of clothing sizes
    SIZE_CHOICES = (
        ('XS', 'XS'),
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL')
    )
        
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="clothing")
    image = models.ImageField(upload_to='images')
    image_data = models.BinaryField(null=True)
    title = models.CharField(max_length=100)
    # notes = models.TextField(max_length=1000, blank=True)
    color = models.CharField(max_length=100, default=COLOR_CHOICES[-1], choices=COLOR_CHOICES)
    size = models.CharField(max_length=100, default=SIZE_CHOICES[-1], choices=SIZE_CHOICES)
    cType = models.CharField(max_length=100, default=CLOTHING_TYPE_CHOICES[-1], choices=CLOTHING_TYPE_CHOICES)
    trade = models.ForeignKey(Trade, on_delete=models.CASCADE, related_name="clothing", null=True, blank=True)
    
    
    

    

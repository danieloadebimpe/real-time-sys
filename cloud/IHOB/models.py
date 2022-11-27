import datetime

from django.db import models
from django.contrib.auth.models import User
from django.core import serializers
import uuid
from django.utils import timezone
# Create your models here.


class Profile(models.Model):
    userID = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, name="user")

    def __str__(self):
        return self.user.name


class Product(models.Model):
    """
        create Product model to be stored in database, with title, image, price, description, left stocks
        Args:
            models.Model: the model template
    """
    productID = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    category = (
        ('NFT', "NFT"),
        ('BlockChain', "BlockChain"),
        ('MetaVerse', "MetaVerse"),
        ('Land', "Land"),
        ('COOPERATION', "COOPERATION"),
        ('Planet', "Planet"),
        ('Vehicle', "Vehicle"),
        ('Camera', 'Camera'),
        ('Lenses','Lenses'),
        ("Computer", "Computer"),
        ("Collab", "Collab"),
    )
    category = models.CharField(choices=category, max_length=20)
    title = models.CharField(max_length=30)
    image = models.ImageField(default=None)
    price = models.IntegerField()
    description = models.TextField()
    seller = models.ForeignKey(User, related_name="seller",  on_delete=models.CASCADE)
    currentHolder = models.ForeignKey(User, related_name="holder",  on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title)


class BiddingItem(models.Model):
    TransactionID = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    ItemId = models.ForeignKey(Product, on_delete=models.CASCADE)
    CurrentPrice = models.FloatField()
    PlaceBidTime = models.DateTimeField(auto_now_add=True)
    CurrentBidder = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.TransactionID)

from django.db import models

# Create your models here.

class User(models.Model):
    class Role(models.IntegerChoices):
        BUYER = 0
        SELLER = 1
        ADMIN = 2
    id = models.BigAutoField(primary_key=True)
    userId = models.CharField(unique=True, null=False, blank=False, max_length=20)
    name = models.CharField(null=False, blank=False, max_length=20)
    password = models.CharField(null=False, blank=False, max_length=20)
    callNumber = models.CharField(null=False, blank=False, max_length=15)
    role = models.SmallIntegerField(null=False, blank=False, default=0, choices=Role.choices)
    address = models.CharField(null=False, blank=False, max_length=200)
    cartItems = models.ManyToManyField('Item', through="Cart")
    
class Cart(models.Model):
    customer = models.ForeignKey("User", on_delete=models.CASCADE, null=False)
    item = models.ForeignKey("Item", on_delete=models.CASCADE, null=False)
    
    amount = models.IntegerField(null=False)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['customer', 'item'], name="oneEntryPerItem"),
        ]

class Order(models.Model):
    id = models.BigAutoField(primary_key=True)
    customer = models.ForeignKey("User", on_delete=models.CASCADE)
    receiverName = models.CharField(null=False, max_length=20)
    receiverNumber = models.CharField(null=False, max_length=15)
    receiverAddress = models.CharField(null=False, max_length=200)
    itemCode = models.ForeignKey("Item", on_delete=models.SET_NULL, null=True)
    amount = models.IntegerField(null=False)
    orderDate = models.DateTimeField(null=False, auto_now_add=True)

class Item(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(null=False, max_length=20)
    price = models.IntegerField(null=False)
    stock = models.IntegerField(null=False)
    sellerid = models.ForeignKey("User", on_delete=models.CASCADE, limit_choices_to={"role": 1})
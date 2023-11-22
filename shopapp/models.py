from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from django.db.models import signals

## admin.py도 참고 바람
class UserManager(BaseUserManager):
    def create_user(self, userName, name, callNumber, address, password=None):
        if not userName:
            raise ValueError("Users must have an UserName")
        if not name:
            raise ValueError("Users must have an name")
        if not callNumber:
            raise ValueError("Users must have an callNumber")
        if not address:
            raise ValueError("Users must have an address")
        
        user = self.model(userName = userName, name = name, callNumber = callNumber, address = address)
        
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, userName, name, callNumber, address, password=None):
        if not userName:
            raise ValueError("Users must have an UserName")
        if not name:
            raise ValueError("Users must have an name")
        if not callNumber:
            raise ValueError("Users must have an callNumber")
        if not address:
            raise ValueError("Users must have an address")
        
        user = self.model(userName = userName, name = name, callNumber = callNumber, address = address)
        
        user.set_password(password)
        user.is_admin = True
        user.save(using=self._db)
        return user
    

class User(AbstractBaseUser):
    userName = models.CharField(primary_key=True, null=False, blank=False, max_length=20)
    name = models.CharField(null=False, blank=False, max_length=20)
    #password = models.CharField(null=False, blank=False, max_length=20)
    callNumber = models.CharField(null=False, blank=False, max_length=15)
    address = models.CharField(null=False, blank=False, max_length=200)
    is_active = models.BooleanField(default=True)
    is_seller = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    
    objects = UserManager()

    USERNAME_FIELD = 'userName'
    #EMAIL_FIELD = ''
    REQUIRED_FIELDS = ['name', 'callNumber', 'address']
    
    def __str__(self):
       return self.userName
   
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

class Item(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(null=False, max_length=20)
    price = models.IntegerField(null=False)
    stock = models.IntegerField(null=False)
    sellerid = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={"is_seller" : True})
    def __str__(self):
       return self.name

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cartItems = models.ManyToManyField(Item, through="CartList")
    def __str__(self):
       return f"{self.user.userName}"

class CartList(models.Model):
    user = models.ForeignKey(Cart, on_delete=models.CASCADE, null=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=False)
    
    amount = models.IntegerField(null=False)
    
    def __str__(self):
       return f"{self.item.name}, {self.amount}"
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'item'], name="oneEntryPerItem"),
        ]

class Order(models.Model):
    id = models.BigAutoField(primary_key=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    receiverName = models.CharField(null=False, max_length=20)
    receiverNumber = models.CharField(null=False, max_length=15)
    receiverAddress = models.CharField(null=False, max_length=200)
    itemCode = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True)
    amount = models.IntegerField(null=False)
    orderDate = models.DateTimeField(null=False, auto_now_add=True)
    def __str__(self):
       return str(self.id)
   
   
from django.dispatch import receiver
@receiver(signals.post_save)
def User_post_creation(sender, instance, created, **kwargs):
    if(sender != User): return
    if(created):
        Cart.objects.create(user = instance)
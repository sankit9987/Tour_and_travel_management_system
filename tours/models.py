from django.db import models
from django.contrib.auth.models import User,AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy  as _
class CustomeUserManger(BaseUserManager):
    def create_user(self,email,password,**extra_fields):
        if not email:
            raise ValueError(_("Email is required"))
        email = self.normalize_email(email)
        user = self.model(email = email,**extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_("super user is "))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_("super user is "))
        return self.create_user(email,password,**extra_fields)

class User(AbstractUser):
    username = None
    email = models.EmailField('emial address' , unique=True)
    password = models.CharField(max_length=16666)
    name= models.CharField(max_length=100)
    Address2= models.CharField(max_length=100)
    Address= models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=12)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zip = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomeUserManger()

    def __str__(self):
        return self.email

class Place(models.Model):
    name= models.CharField(max_length=100)
    des= models.CharField(max_length=100)
    cost= models.CharField(max_length=100)
    image= models.ImageField(upload_to='place')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

sta = (
    ('confirm','confirm'),
    ('cancel','cancel'),
)
class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    travel_date = models.DateField()
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zip = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    card_name = models.CharField(max_length=100)
    card_number = models.CharField(max_length=100)
    exp_mon = models.CharField(max_length=100)
    exp_year = models.CharField(max_length=100)
    cvv = models.CharField(max_length=100)
    status = models.CharField(max_length=100,choices=sta,null=True)


class Contact(models.Model):
    name= models.CharField(max_length=100)
    mobile= models.CharField(max_length=100)
    email= models.CharField(max_length=100)
    msg= models.CharField(max_length=100)
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.models import AbstractUser
from django_resized import ResizedImageField
from .models import *


class CustomUser(AbstractUser):
    username = models.CharField(max_length=255, blank=True, null=True, unique=True)
    email = models.EmailField(max_length=255, blank=True, null=True, unique=True)
    mobile_number = models.CharField(max_length=14, null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True, editable=False, blank=True)
       
       
class Owner(CustomUser):
    image = models.ImageField(upload_to='renteloo_app/profile_images', default='renteloo_app/profile_images/profile.png', blank=True, null=True)
    is_owner = models.BooleanField(default=True)
   
    class Meta:
        verbose_name_plural = 'Owner Database'
   
    def __str__(self):
        return self.username
    
    
class Tenant(CustomUser):
    image = models.ImageField(upload_to='renteloo_app/profile_images', default='renteloo_app/profile_images/profile.png', blank=True, null=True)
    is_tenant = models.BooleanField(default=True)
   
    class Meta:
        verbose_name_plural = 'Tenant Database'
    
    def __str__(self):
        return self.username
    
    
class Room(models.Model):
    NUMBER_OF_ROOMS = (
        ("1R", "1R"),
        ("1RK", "1RK"),
        ("2Rk", "2Rk"),
        ("3Rk", "3Rk"),
        ("4Rk", "4Rk"),
        ("5Rk", "5Rk"),
        ("6Rk", "6Rk"),
    )
    
    TENANT_PREFER = (
        ("Family", "Family"),
        ("Female Students", "Female Students"),
        ("Male Students", "Male Students"),
        ("Open For All", "Open For All")
    )
    
    BATH_CHOICES = (
        ("Attached", "Attached"),
        ("Shared", "Shared")
    )
    
    E_BILL = (
        ("Self Payement", "Self Payement"),
        ("Included In Rent", "Included In Rent"),
        
    )
    
    STATUS_CHOICES =(
        ("Available", "Available"),
        ("Booked", "Booked"),
    )
    image1 = ResizedImageField(size=[500, 300], upload_to='renteloo_app/room_images', default='renteloo_app/room_images/room.png', blank=True, null=True)
    image2 = ResizedImageField(size=[500, 300], upload_to='renteloo_app/room_images', default='renteloo_app/room_images/room.png', blank=True, null=True)
    image2 = ResizedImageField(size=[500, 300], upload_to='renteloo_app/room_images', default='renteloo_app/room_images/room.png', blank=True, null=True)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    price_per_month = models.IntegerField(default=None)
    address = models.CharField(max_length=200, blank=False)
    pin_code = models.CharField(max_length=6, blank=True)
    tenant_preference = models.CharField(max_length=20, choices=TENANT_PREFER, blank=True, default="Open For All")
    rooms = models.CharField(max_length=20, choices=NUMBER_OF_ROOMS)
    bath_room = models.CharField(max_length=20, choices=BATH_CHOICES, blank=True, default="Open For All")
    floor = models.CharField(max_length=20, blank=True, null=True)
    electric_bill = models.CharField(max_length=20, choices=E_BILL, default="Included In Rent")
    room_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Available")
    other_details = models.TextField(max_length=500)
    listed_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "room"

    def __str__(self):
        return str(self.id) +"-"+ str(self.rooms) +"-"+ self.address +"-"+ str(self.price_per_month)

class Booking(models.Model):
    tenant = models.OneToOneField(Tenant, related_name="booking", on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Booking"
    
    def __str__(self):
        return str(self.tenant)
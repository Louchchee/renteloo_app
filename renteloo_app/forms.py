from django.forms import ModelForm
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm 
from .models import Room, Booking, CustomUser, Owner, Tenant
from django.forms.forms import Form
from django import forms
from django.core.exceptions import ValidationError  
from django.forms.fields import EmailField 



class OwnerUserCreationForm(UserCreationForm):
    class Meta:
        model = Owner
        fields = "__all__"
        
        
class TenantUserCreationForm(UserCreationForm):
    class Meta:
        model = Tenant
        fields = "__all__"
        
       
class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = "__all__"
        
        
class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = "__all__"
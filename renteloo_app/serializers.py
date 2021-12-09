from rest_framework import serializers
from django.contrib.auth.models import Group
from renteloo_app.models import *


class OwnerRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = Owner
        fields =['username', 'email', 'password', 'password2']
        extra_kwrags = {'password': {'write_only': True}}

    def save(self):
        owner = Owner(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        
        if password != password2:
            raise serializers.ValidationError("Password must match.")
        owner.set_password(password)
        owner.save()
        
    
class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = '__all__'



class TenantRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = Tenant
        fields =['username', 'email', 'password', 'password2']
        extra_kwrags = {'password': {'write_only': True}}

    def save(self):
        tenant = Tenant(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        
        if password != password2:
            raise serializers.ValidationError("Password must match.")
        tenant.set_password(password)
        tenant.save()
        return tenant

        
class TenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'
        
        
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'user', 'room_id', 'room', 'booking_date']
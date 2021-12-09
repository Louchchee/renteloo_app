from django.contrib import admin
from django.contrib.auth.models import User
from .models import CustomUser, Owner, Tenant, Room, Booking
from .models import CustomUser
from .forms import OwnerUserCreationForm, TenantUserCreationForm
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class OwnerUserAdmin(UserAdmin):
    models = Owner
    readonly_fields = ['date_joined']
    add_form = OwnerUserCreationForm
    list_display = ('id', 'username', 'email','date_joined')
    
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'User role',
            {
                'fields':(
                    'is_owner',
                )
            }
        )
    )

        
class TenantUserAdmin(UserAdmin):
    models = Tenant
    readonly_fields = ['date_joined']
    add_form = TenantUserCreationForm
    list_display = ('id', 'username', 'email','date_joined')
    
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'User role',
            {
                'fields':(
                    'is_tenant',
                )
            }
        )
    )
 

class RoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'rooms', 'price_per_month', 'address', 'tenant_preference', 'bath_room', 'floor', 'electric_bill', 'room_status', 'listed_on')
    
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'tenant', 'room', 'booking_date')

admin.site.register(Owner, OwnerUserAdmin)
admin.site.register(Tenant, TenantUserAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Booking, BookingAdmin)
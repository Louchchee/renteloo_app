from django.urls import path
from rest_framework import routers
from . import api_views as views


app_name = 'renteloo_app'

urlpatterns = [
    #API URLS
    
    path('owner/register/', views.ownerRegisterView),
    path('tenant/register/', views.tenantRegisterView),
   
   #NORMAL URLS
    path('login/', views.userLogin, name='login'),
    path('logout/', views.userLogout, name='logout'),
    path('owner-register/', views.ownerRegister, name='owner-register'),
    path('tenant-register/', views.tenantRegister, name='tenant-register'),
    
    path('profile/<str:pk>/', views.userProfile, name='user-profile'),

    path('', views.home, name='home'),

    path('booking/', views.bookRoom, name='booking'),
    path('booking-list/', views.bookingListView, name="booking-list"),
    path('booking-detail/<str:pk>/', views.bookingDetailView, name="booking-detail"),
    path('delete-booking/<str:pk>/', views.deletebooking, name="delete-booking"),
    
    path('room/<str:pk>/', views.room, name="room"),
    path('create-room/', views.createRooms, name='create-room'),
    path('update-room/<str:pk>/', views.updateRooms, name="update-room"),
    path('delete-room/<str:pk>/', views.deleteRooms, name="delete-room"),
    
]

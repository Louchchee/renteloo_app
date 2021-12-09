"""renteloo_core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import  include, path
from rest_framework import routers
from renteloo_app import api_views as views


router = routers.DefaultRouter()
router.register(r'owners', views.OwnerViewSet),
router.register(r'tenants', views.TenanatViewSet),
router.register(r'rooms', views.RoomsViewSet)
router.register(r'rooms-action', views.AddRoomsViewSet)
router.register(r'bookings', views.BookingViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('renteloo_app.urls', 'renteloo_app_api')),

]
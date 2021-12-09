from rest_framework import serializers, viewsets
from rest_framework import permissions
from django.contrib.auth.models import Group
from rest_framework.decorators import api_view
from rest_framework.response import Response
from renteloo_app.models import *
from .serializers import *
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions

@api_view(['POST'])
def ownerRegisterView(request):
    if request.method == 'POST':
        serializer = OwnerRegisterSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            owner = serializer.save()
            group = Group.objects.get(name="Owner")
            owner.groups.add(group)
            
            data['response'] = "Successfully  registered a new owner."
            data['email'] = owner.email
            data['username'] = owner.username
        else:
            data = serializer.errors
        return Response(data)
    
class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


@api_view(['POST'])
def tenantRegisterView(request):
    if request.method == 'POST':
        serializer = TenantRegisterSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            tenant = serializer.save()
            group = Group.objects.get(name="Tenant")
            tenant.groups.add(group)
            
            data['response'] = "Successfully  registered a new tenant."
            data['email'] = tenant.email
            data['username'] = tenant.username
        else:
            data = serializer.errors
        return Response(data)

class TenanatViewSet(viewsets.ModelViewSet):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class RoomsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    
    
class AddRoomsViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
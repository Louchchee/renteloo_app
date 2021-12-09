from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from .forms import  OwnerUserCreationForm, TenantUserCreationForm, RoomForm, BookingForm
from django.contrib.auth.models import Group, Permission, User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Room, Booking



# Create your views here.
def userLogin(request):
    page = 'login'
    if request.user.is_authenticated :
        return redirect("home")

    else:
        if request.method == "POST":
        #turn username into lower and assign to username variable
            username = request.POST.get("username").lower()
            email = request.POST.get("email")
            #assign requested password to password variable
            password = request.POST.get("password")
    
            user = authenticate(request, username = username, email=email, password = password)

            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                messages.error(request, "Username or password does not match, please try again!")
    context={'page':page}
    return render(request, 'renteloo_app/login_register.html', context)


def userLogout(request):
    logout(request)
    return redirect('home')


def ownerRegister(request):
    #register user
    form = OwnerUserCreationForm()
    if request.method == "POST":
        form = OwnerUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")
            
            group = Group.objects.get(name="Owner")
            user.groups.add(group)
            return redirect("login") 
        
    context = {'form':form}
    return render(request, 'renteloo_app/login_register.html', context)


def tenantRegister(request):
    #register user
    form = TenantUserCreationForm()
    if request.method == "POST":
        form = TenantUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")
            
            group = Group.objects.get(name="Tenant")
            user.groups.add(group)
            return redirect("login") 

    context = {'form':form}
    return render(request, 'renteloo_app/login_register.html', context)
        
        
def userProfile(request, pk):
    user = User.objects.get(id=pk)
    rooms = user.room_set.all()
    room_count = rooms.count()
    context = {'user':user, 'rooms':rooms, 'room_count':room_count}
    return render(request, 'renteloo_app/profile.html', context)


def home(request):
    rooms = Room.objects.all()
    room_count = rooms.count() 
    context={"rooms":rooms}
    return render(request, 'renteloo_app/home.html', context)


def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room':room}
    return render(request, 'renteloo_app/rooms.html', context)


@login_required(login_url='login')
def bookRoom(request):
    form = BookingForm
    user = User.objects.all()
    room = Room.objects.all()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect("home")
        
    context = {"form":form, 'user':user, 'new_room':new_room}
    return render(request, 'renteloo_app/booking_form.html', context)
       
 
def bookingListView(request):
    booked_room = Booking.objects.all()
    context = {'booked_room':booked_room}
    return render(request, 'renteloo_app/booked.html', context)


def bookingDetailView(request, pk):
    booking = Booking.objects.get(id=pk)
    context = {'booking':booking}
    return render(request, 'renteloo_app/booking_detail.html', context)


def deletebooking(request, pk):
    booked_room = Booking.objects.get(id=pk)
    
    if request.user != booked_room.user:
        return HttpResponse("You are not authorized to delete this booking.")
    
    if request.method == 'POST':
        booked_room.delete()
        return redirect("booking")
    
    context = {"booked_room":booked_room}
    return render(request, 'renteloo/delete.html', context)


@login_required(login_url='login')
def createRooms(request):
    form = RoomForm()
    user = User.objects.all()
    groups = Group.objects.filter(user=request.user)

    for user_group in groups:
        if user_group.name == "Owner":
            if request.method == 'POST':
                form = RoomForm(request.POST)
            
                if form.is_valid():
                    form.save()
                return redirect("home")
        else:
            return HttpResponse("You are not authorized, please login/register as owner and try again!")

    context = {"user":user, "form":form}
    return render(request, 'renteloo_app/room_form.html', context)



@login_required(login_url='login')
def updateRooms(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    
    if request.user != room.owner:
        return HttpResponse("You are not allowed to update.")
    
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        
        if form.is_valid():
            form.save()
            return redirect("home")
    context={"form":form, 'room':room}
    return render(request, 'renteloo_app/room_form.html', context)


@login_required(login_url='login')
def deleteRooms(request, pk):
    room = Room.objects.get(id=pk)
    
    if request.user != room.owner:
        return HttpResponse("You are not allowed to delete.")
   
    if request.method == 'POST':
        room.delete()
        return redirect("home")
    
    context = {"obj":room}
    return render(request, 'renteloo_app/delete.html', context)
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
import requests
from .models import FollowerCounter
from .forms import CustomUserForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def homePage(request):
    currentNativeUser = request.GET.get('user')
    logged_in_user = request.user.username
    userFollowers = len(FollowerCounter.objects.filter(user=currentNativeUser))
    userFollowing = len(FollowerCounter.objects.filter(follower=currentNativeUser))
    userFollowers_A = FollowerCounter.objects.filter(user=currentNativeUser)
    userfollowers_B = []
    for i in userFollowers_A:
        userFollowers_A = i.follower
        userfollowers_B.append(userFollowers_A)
    if logged_in_user in userFollowers_A:
        followButtonValue = 'unfollow'
    else:
        followButtonValue = 'follow'
    return render(request, 'base/homePage.html', {
        'current_user': currentNativeUser,
        'user_followers': userFollowers,
        'user_following': userFollowing,
        'follow_button_value': followButtonValue
    })

def followersCount(request):
    if request.method == 'POST':
        value = request.POST['value']
        user = request.POST['user']
        follower = request.POST['follower']
        if value == 'follow':
            followersCount = FollowerCounter.objects.create(follower=follower, user=user)
            followersCount.save()
        else:
            followersCount = FollowerCounter.objects.get(follower=follower, user=user)
            followersCount.delete()
        
        return redirect('/?user='+user)



def registerPage(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect('/')
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = CustomUserForm()
    context = {
        'registrationForm' : form
    }
    return render(request, 'base/registerPage.html', context)
            
            

def loginPage(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("/")
            else:
                messages.error(request,"Invalid username or password.")

        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    context = {
        'loginForm' : form
    }
    return render(request,  'base/loginPage.html', context)


def logoutPage(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("/")

def profilePage(request):
    return render(request, 'base/profilePage.html' )


def followPage(request):
    return render(request, 'base/followPage.html' )
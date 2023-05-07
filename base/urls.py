from django.urls import path
from . import views


urlpatterns = [
    path('', views.homePage, name="homePage"),
    path('followers_count', views.followersCount, name='followers_count'),
    path('registerPage', views.registerPage, name="registerPage"),
    path('loginPage', views.loginPage, name="loginPage"),
    path('logoutPage', views.logoutPage, name="logoutPage"),
    path('profilePage', views.profilePage, name="profilePage"),
    path('followPage', views.followPage, name="followPage"),
]


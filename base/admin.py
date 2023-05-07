from django.contrib import admin
from .models import FollowerCounter, Profile

# Register your models here.

admin.site.register(FollowerCounter)
admin.site.register(Profile)
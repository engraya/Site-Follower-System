from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class FollowerCounter(models.Model):
    user = models.CharField(max_length=50)
    follower = models.CharField(max_length=50)
    comment = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullName = models.CharField(max_length=200)
    phone = models.IntegerField(null=True, blank=True)
    homeAddress = models.CharField(max_length=200)
    profile_pic = models.ImageField(default='git.png',upload_to='images')
    bio = models.TextField()
    date_of_birth = models.DateField(null=True, blank=True)
    profession = models.CharField(max_length=200)
    website = models.URLField(null=True, max_length=200)
    github = models.URLField(null=True, max_length=200)
    twitter = models.URLField(null=True, max_length=200)
    instagram = models.URLField(null=True, max_length=200)
    facebook = models.URLField(null=True, max_length=200)

    def __str__(self):
        return f'{self.user.username} Profile'


    def save(self):
        super().save()

        img = Image.open(self.profile_pic.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)



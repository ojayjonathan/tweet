from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class User (AbstractBaseUser):
    username = models.CharField('username', max_length=10, unique=True, db_index=True)
    email = models.EmailField('email address', unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    profile_pic = models.ImageField(blank=True, null=True)
    DOB = models.DateField(null=True)
    country = models.CharField(max_length=30, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    joined = models.DateField(auto_now=True)

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username


class Following(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    following = models.ManyToManyField(User, related_name='follow_me')

    def __str__(self):
        return self.following


class Followers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    follower = models.ManyToManyField(User, related_name='follower')

    def __str__(self):
        return self.follower






from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class User (AbstractBaseUser):
    username = models.CharField('username', max_length=10, unique=True, db_index=True)
    email = models.EmailField('email address', unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    profile_pic = models.ImageField(blank=True, default='user.png', upload_to='images')
    thumbnail = ImageSpecField(source='profile_pic', processors=[ResizeToFill(200, 200)], format="jpeg",
                               options={'quality': 60})
    DOB = models.DateField(null=True)
    country = models.CharField(max_length=30, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    joined = models.DateField(auto_now=True)

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username


class FollowingUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name="follow_you")

    def __str__(self):
        return self.following


class FollowersUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="follow_me")
    follower = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user






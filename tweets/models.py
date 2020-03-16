from django.db import models
from user_profile.models import User


class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=160)
    created_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    tweet_file = models.FileField(null=True)

    def __str__(self):
        return self.text


class Hashtag (models.Model):
    name = models.CharField(max_length=60, unique=True)
    tweet = models.ManyToManyField(Tweet)

    def __str__(self):
        return self.name



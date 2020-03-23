from django.db import models
from user_profile.models import User
from imagekit.processors import ResizeToFill
from imagekit.models import ProcessedImageField, ImageSpecField


class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=160)
    created_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(null=True, blank=True, upload_to='images')
    tweet_file = models.FileField(null=True, blank=True, upload_to='videos')
    image_thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(350, 250)],
                                     options={'quality': 60})

    def __str__(self):
        return self.text


class Hashtag (models.Model):
    name = models.CharField(max_length=60, unique=True)
    tweet = models.ManyToManyField(Tweet)
    hashtag_count = models.IntegerField(default=1)

    def __str__(self):
        return self.name

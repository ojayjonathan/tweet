from django.views.generic import View
from .admin import User
from django.shortcuts import render
from .models import Followers, Following
from tweets.models import Tweet
from django.shortcuts import get_object_or_404


class Profile(View):

    def get(self, request, username):
        user = get_object_or_404(User, username=username)
        id = user.id
        followers = Followers.objects.filter(user=user).count()
        following = Following.objects.filter(user=user).count()
        tweets_count = Tweet.objects.filter(user=user).count()
        tweets = Tweet.objects.filter(user=user)
        context = {
            'user': user,
            'followers': followers,
            'following': following,
            'tweets_count': tweets_count,
            'tweets': tweets,
            'Tweet': Tweet
        }

        return render(request, 'user_profile/details.html', context)








from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.views import View
from .models import Tweet, Hashtag
from user_profile.models import User
from .forms import TweetForm

from django.http import HttpResponseRedirect


class HomeView(View):

    def get(self, request, username):
        user = User.objects.get(username=username)
        context = {
            'user': user
        }
        return render(request, 'home.html', context)


class TweetView(View):

    def post(self, request, username):
        form = TweetForm(self.request.POST)
        if form.is_valid():
            user = User.objects.get(username=username)
            text = form.cleaned_data['text']
            tweet_file = form.cleaned_data['tweet_file']
            tweet = Tweet(text=text, user=user, tweet_file=tweet_file)
            tweet.save()
            words = text.split()
            for word in words:
                if word[0] == "#":
                    hashtag, created = Hashtag.objects.get_or_create(name=word[1:])
                    hashtag.tweet.add(tweet)

            return HttpResponseRedirect('/home/' + username)
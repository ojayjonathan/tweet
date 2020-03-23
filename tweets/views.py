from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.views import View
from .models import Tweet, Hashtag
from user_profile.models import User
from .forms import TweetForm, SearchForm

from django.http import HttpResponseRedirect
from tweets.models import Tweet
import subprocess


class HomeView(View):

    def get(self, request, username):
        user = User.objects.get(username=username)
        tweets = Tweet.objects.filter(user=user)
        q = request.GET.get('q', None)
        if q is not None and q is not "":
            tweet_result = Tweet.objects.filter(text__icontains=q)
            user_result = User.objects.filter(username__icontains=q)
            context = {
                'user': user,
                'tweets': tweets,
                'tweet_result': tweet_result,
                'user_result': user_result
            }
        elif q is None or q is '':
            context = {
                'user': user,
                'tweets': tweets,
            }

        return render(request, 'base/base.html', context)


class TweetView(View):

    def post(self, request, username):
        form = TweetForm(self.request.POST, request.FILES)
        if form.is_valid():
            user = User.objects.get(username=username)
            text = form.cleaned_data['text']

            image = form.cleaned_data['image']
            tweet_file = form.cleaned_data['tweet_file']
            tweet = Tweet(text=text, user=user, tweet_file=tweet_file, image=image)
            tweet.save()
            words = text.split()
            for word in words:
                if word[0] == "#":
                    hashtag, created = Hashtag.objects.get_or_create(name=word[1:], hashtag_count=+1)
                    hashtag.tweet.add(tweet)

            return HttpResponseRedirect('/home/' + username)
        else:
            form = TweetForm()
            user = User.objects.get(username=username)
            tweets = Tweet.objects.filter(user=user)
            tweet_ers = 'invalid tweet'
            context = {
                'user': user,
                'form': form,
                'tweets': tweets,
                'tweet_ers': tweet_ers
            }
            return render(request, 'base/base.html', context)




from django.views.generic import View
from .admin import User
from django.shortcuts import render
from .models import FollowersUser, User
from tweets.models import Tweet
from django.shortcuts import get_object_or_404
from tweets.forms import SearchForm, LoginForm
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect


class Profile(View):
    @staticmethod
    def get(request, username):
        user = get_object_or_404(User, username=username)
        followers_count = FollowersUser.objects.filter(user=user).count()
        followers = FollowersUser.objects.filter(user=user)
        tweets_count = Tweet.objects.filter(user=user).count()
        tweets = Tweet.objects.filter(user=user)
        q = request.GET.get('q', None)
        if q is not None and q is not "":
            tweet_result = Tweet.objects.filter(text__icontains=q)
            user_result = User.objects.filter(username__icontains=q)
            context = {
                'user': user,
                'followers_count': followers_count,
                'tweets_count': tweets_count,
                'tweets': tweets,
                'Tweet': Tweet,
                'followers': followers,
                'tweet_result': tweet_result,
                'user_result': user_result
            }
        elif q is None or q is "":
            context = {
                'user': user,
                'followers_count': followers_count,
                'tweets_count': tweets_count,
                'tweets': tweets,
                'Tweet': Tweet,
                'followers': followers,
            }

        return render(request, 'user_profile/details.html', context)


class Login(View):
    context = {}

    @staticmethod
    def get(request):
        return render(request, 'user_profile/login.html', context={})

    @staticmethod
    def post(request):
        form = LoginForm(request.POST)
        if form.is_valid:
            username = form['username']
            password = form['password']
            #user = authenticate(request, username=username, password=password)
            user = User.objects.filter(username=username)
            if user:
                login(request, password=password, username=username)
            else:
                msg = 'Invalid login Details'
                context = {
                    'form': form,
                     'msg': msg
                }
                return render(request, 'user_profile/login.html', context)
            return HttpResponseRedirect('/home/'+user.username)


class Logout(View):
    pass





from django.urls import path
from .views import HomeView, TweetView

app_name = 'tweet'

urlpatterns = [
    path('<username>/', HomeView.as_view(), name='home'),
    path('<username>/post', TweetView.as_view(), name='post'),
]
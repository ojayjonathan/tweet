from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'user_profile'

urlpatterns = [
    path('<username>/', views.Profile.as_view(), name='profile'),
    path('auth/login/', views.Login.as_view(), name='login'),
    path('<username>/logout/', views.Logout.as_view(), name='logout'),

]
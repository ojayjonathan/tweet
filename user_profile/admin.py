from django.contrib import admin
from .models import User, Followers, Following

admin.site.register(User)
admin.site.register(Following)
admin.site.register(Followers)


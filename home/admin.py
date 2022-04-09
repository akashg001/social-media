from django.contrib import admin
from .models import user_post,user_profile
# Register your models here.
admin.site.register(user_profile)
admin.site.register(user_post)

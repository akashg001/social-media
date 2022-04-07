from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('login/',views.login,name="login"),
    path('register/',views.register,name="register"),
    path('profile/',views.profile,name="profile"),
    path('profile_edit/',views.profile_edit,name="profile_edit"),
    path('post/',views.post,name="post"),
    path('handle_register/',views.handle_register,name="handle_register"),
    path('handlelogin/',views.handlelogin,name="handlelogin"),
    path('post/',views.post,name="post"),
    path('upload/',views.upload,name="upload")
    
 ]

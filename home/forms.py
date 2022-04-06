from django.db import models
from django.forms import fields
from .models import user_post
from django import forms

class postimage(forms.ModelForm):
    class meta:
        models=user_post
        fields='__all__'
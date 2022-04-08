from django import forms
from .models import user_post
class postimage(forms.Form):
  
    class Meta:
        model = user_post
        fields=['image','caption']
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.conf import settings
from django.db.models.signals import post_save
from django.utils.text import slugify
from taggit.managers import TaggableManager

def user_directory_path(instance, filename):
    return'user-{0}/{1}'.format(instance.user.id,filename)
   
class user_post(models.Model):
    user = models.ForeignKey(User,default = 1, on_delete=models.CASCADE)
    feed = models.ImageField(upload_to='uploads', blank=True)
    likes= models.BigIntegerField()
    comment = models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now=True, auto_now_add=True)
    slug= models.SlugField(unique=True, null=False)
    tags= models.TaggableManager()
    class meta:
        db_table:'userpost'


class user_profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    dob=models.DateField(auto_now=True, auto_now_add=False)
    country = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    dp = models.ImageField(upload_to='profile_image', blank=True)
    #phone = models.PhoneNumberField(_(""))
    def __str__(self):
        return self.user.username
    
from django.shortcuts import render,HttpResponse,redirect
from .models import user_profile,user_post
from django.contrib.auth.models import User
from django.contrib.auth import login as dj_login
from django.contrib.auth import authenticate
from home.forms import postimage


def index(request):
    return HttpResponse("this is social media")
def login(request):
    return render(request,'home/login.html')
def register(request):
    return render(request,'home/register.html')
def profile(request):
    return HttpResponse("this is profile page")
def profile_edit(request):
    return HttpResponse("this is profile edit page")
def post(request):
    if request.session.has_key('is_logged'):
        if request.method=='POST':
            form=postimageform(request.POST,request.FILES)
            form.save()

def handle_register(request):
    if request.method == 'POST':
        uname=request.POST['uname']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        country=request.POST['country']
        dob=request.POST['dob']
        #phone=request.POST['phone']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        
        profile = user_profile(country=country,dob=dob)

        user=User.objects.create_user(uname,email,pass1)
        user.first_name=fname
        user.last_name=lname
        user.email=email
        #user.phone=phone

        user.save()
        profile.user=user
        profile.save()
        return redirect('/')
    else:
        return HttpResponse("404")
    return redirect('/login')

def handlelogin(request):
    if request.method=='POST':
        loginuname=request.POST.get("loginuname")
        loginpassword1=request.POST.get("loginpassword1")
        user=authenticate(username=loginuname,password=loginpassword1)
        if user is not None:
            dj_login(request,user)
            request.session['is_logged']=True
            user=request.user.id
            request.session["user_id"]=user
            return redirect('/')
        else:
            return redirect('/login')
        return HttpResponse("404")
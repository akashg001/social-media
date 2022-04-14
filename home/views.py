from django.shortcuts import render,HttpResponse,redirect
import pyrebase

config = {
    "apiKey": "AIzaSyDd738Oycvch0gXs8rw7K-i31fOg_xJLdQ",
    "authDomain": "social-media-3df5c.firebaseapp.com",
    "projectId": "social-media-3df5c",
    "storageBucket": "social-media-3df5c.appspot.com",
    "messagingSenderId": "150668275038",
    "appId": "1:150668275038:web:489d68701f9caf6c8c33cf",
    "measurementId": "G-YJ0J37234B",
    "databaseURL": ""
  }

firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()

def index(request):
    #request.POST['caption'] = caption
    #request.FILES['image'] = image
    #context = {'caption':caption,'image':image}
    #return render(request,'home/dashboard.html',context)
    return HttpResponse("this is social media")
def login(request):
    return render(request,'home/login.html')
def register(request):
    return render(request,'home/register.html')
def upload(request):
    return render(request,'home/post_image.html')
def profile(request):
    return HttpResponse("this is profile page")
def profile_edit(request):
    return HttpResponse("this is profile edit page")
def post(request):
    #if request.session.has_key('is_logged'):
     #   if request.method=='POST':
      #      caption=request.POST['caption']
       #     image = request.FILES['image']
        #    files = user_post(caption = caption,image = image)
         #   files.save()
         #   return redirect('/<caption><image>')
            
        #else:
         #   return HttpResponse("not uploaded")
        #files=user_post()
        #return render(request,'home/dashboard.html',{'files':files})
    #else:
    return HttpResponse("not logged in")

def handle_register(request):
    fname=request.POST.get('fname')
    lname=request.POST.get('lname')
    email=request.POST.get('email')
    country=request.POST.get('country')
    dob=request.POST.get('dob')
    #phone=request.POST['phone']
    pass1=request.POST.get('pass1')
    pass2=request.POST.get('pass2')
    try:
        user = authe.create_user_with_email_and_password(email,pass1)
        uid = user['localId']
        idtoken = request.session['uid']
        print(uid)
        return render(request,"home/login.html")
    except:
        return render(request,"home/register.html")

def handlelogin(request):
    email = request.POST.get('email')
    pasw = request.POST.get('pass')
    try:
        user=authe.sign_in_with_email_and_password(email,pasw)
    except:
        message="Invalid Credentials!! please check details"
        return render(request,"home/login.html",{"message":message})
    session_id = user['idToken']
    request.session['uid']=str(session_id)
    return render(request,"home/dashboard.html",{"email":email})
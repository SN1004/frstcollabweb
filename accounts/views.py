from django.shortcuts import render,redirect 
from django.contrib import messages
from django.contrib.auth.models import User, auth 
# Create your views here.

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if pass1 == pass2 :
            if User.objects.filter(username=username).exists():
                messages.info(request,'\nusername taken.\n')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'\nemail taken.\n')
                return redirect('register')
            else :
                user = User.objects.create_user(username=username , first_name = first_name , last_name = last_name , password = pass1 , email = email )
                user.save();
                messages.info(request,'\nuser created!!\n')
                return redirect('register')
        else : 
            messages.info(request,'\npassword not matched.\n')
            return redirect('register')
    else:
        return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        usercheck= auth.authenticate(username = username,password = password)
        if usercheck is not None:
            auth.login(request, usercheck)
            return redirect('/')
        else:
            messages.info(request,'\nInvalid username or password.\n')
            return redirect('login')

    else:
        return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')
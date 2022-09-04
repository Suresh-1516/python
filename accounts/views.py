
from django.contrib import messages  
from django.shortcuts import redirect, render

from django.contrib.auth.models import User , auth

# Create your views here.


def login(request):
    
    if request.method == 'POST':
            
        username = request.POST['login_username']
        password1 = request.POST['login_password']

        user = auth.authenticate(username=username,password=password1)

        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"Invalid User & Password")
            return redirect('login')

    
    else:
        return render(request,'login.html')



def register(request):
    

    if request.method == 'POST':
    
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        # Email = request.POST['email']

        if password1 == password2:    
        
            if User.objects.filter(username=username).exists():
                messages.info(request,"USERNAME IS ALLREDY TAKEN :(")
                return redirect('register')
                    
            else:

                user = User.objects.create_user(username=username,password=password1,first_name=first_name,last_name=last_name)
                user.save();
                return redirect('login')
                print("User Created :)")
        
        else:
            messages.info(request,"Password Not Match")
            return redirect('register')



    else:
        return render(request,"reg.html")


def logout(request):
    auth.logout(request)
    return redirect ('/')
    
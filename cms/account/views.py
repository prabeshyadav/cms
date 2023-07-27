from django.shortcuts import render
from cms import  common
from django.contrib.auth.hashers import make_password
from .models import *
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import CustomerRegister

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Replace 'home' with the URL name of your home page
        else:
            # Authentication failed, show an error message
            error_message = 'Invalid login credentials. Please try again.'
            return render(request, 'account/login.html', {'error_message': error_message})
    else:
        return render(request, 'account/login.html')


def user_logout(request):
    logout(request)
    return redirect('home') 


def home(request):
    return render(request,'account/home.html')

def Register(request):
    data={
        'role':common.USER_ROLES
    }
    
    if request.methon=="POST":
        form=CustomerRegister(request.POST)
        if form.is_valid():
            user_data = {
                'username': form.cleaned_data.get('username'),
                'name': form.cleaned_data.get('name'),
                'email': form.cleaned_data.get('email'),
                'address':form.cleaned_data.get('address'),
                'phone_number': form.cleaned_data.get('phone_number'),
                'role': form.cleaned_data.get('role'),
            }
            password=make_password(request.POST['password'])
            user=CustomUser.objects.create(password=password,**user_data)
            
            return redirect('')
        
        


    else:
        form=CustomUser()
        
    context={
        'data':data,
        'form':form,
    }
    return render(request,'',context)
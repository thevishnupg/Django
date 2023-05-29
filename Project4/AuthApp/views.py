from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from AuthApp.models import CustomUser
from AuthApp.form import CustomUserCreationForm

# Create your views here.

def base(request):
    return render(request,'base.html')

def home(request):
    return render(request,'home.html')

def sign1_up(request):
    form = CustomUserCreationForm()
    if (request.method=='POST'):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return home(request)
    return render(request, 'sign_up.html',{'form':form})

def log_in(request):
    if (request.method=='POST'):
        name = request.POST['n']
        password = request.POST['p']
        user = authenticate(username=name,password=password)
        if user:
            login(request,user)
            return home(request)
        else:
            return HttpResponse('Invalid User')
    return render(request,'log_in.html')

def log_out(request):
    logout(request)
    return log_in(request)



# def pass_change(request):
#     pass

# def pass_change_done(request):
#     return render(request,'pass_ch_done.html')
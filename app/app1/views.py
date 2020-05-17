from django.shortcuts import render
from .forms import ff,ff1
from .models import kk
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
# from django.urls import reverse
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request,'home.html')

def reg(request):
    print('hello')
    obj=ff()
    obj1=ff1()
    if request.method=='POST':
        print('hi')
        obj=ff(request.POST)
        obj1=ff1(request.POST)
        if obj.is_valid() and obj1.is_valid():
            x=obj.save(commit=True)
            x.is_superuser=True


            x.is_staff = True
            x.set_password(x.password)
            x.save()
            print(x.password)
            y=obj1.save(commit=False)
            y.use=x

            if 'display_pic' in request.FILES:
                y.display_pic=request.FILES['display_pic']
            y.save()

    return render(request, 'reg.html', {'f1':obj,'f2':obj1})



def user_login(request):
    if request.method=='POST':
        n=request.POST.get('name')
        p=request.POST.get('pass')
        user_obj=authenticate(username=n,password=p)
        if user_obj is not None:
            if user_obj.is_active:
                login(request,user_obj)
                request.session['username']=user_obj.username
                return home(request)
            else:
                return HttpResponse('not active')
        else:
            return HttpResponse('invalid')
    return render(request, 'logins.html')


@login_required
def user_logout(request):
        del request.session['username']
        logout(request)
        return reg(request)

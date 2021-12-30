from django.shortcuts import render
from django.http import HttpResponse
from projectapp.models import *


def home(request):
    return render(request,'index.html')


def reg(request):
    if request.method =='POST':
        myemail=request.POST['email']
        mypsw=request.POST['psw']
        mypsw2=request.POST['re_type']
        frstname=request.POST['fname']
        lname=request.POST['lname']
        gender=request.POST['st']
        country=request.POST['country']
        info=registration_tb(email=myemail,password=mypsw,re_password=mypsw2,first_name=frstname,last_name=lname,gender=gender,country=country)
        info.save()
        # return render(request,'index.html')
        return HttpResponse("Successfully registered")

    else:
        return render(request,'index.html')
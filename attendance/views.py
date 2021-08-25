from django.http import request
from django.shortcuts import redirect, render, resolve_url
from datetime import datetime
from attendance.models import Attend
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    return render(request, "home.html")

def attendance(request):   
    if request.method == "POST":
        name = request.POST.get('name')
        roll = request.POST.get('roll')
        subject = request.POST.get('subject')
        time = datetime.today()     
        action = Attend(name=name, roll= roll, subject=subject, date=time)
        action.save()
        messages.success(request, 'your data has been submited')
    return render(request, "attendance.html")

def studentinfo(request):
    return render(request,"studentinfo.html")

def userlogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username= username, password=password)
        if user is not None:
            login(request,user)
            return render(request, 'home.html')
    return render(request,'userlogin.html')

def userlogout(request):
    logout(request)
    return render(request, 'userlogin.html')
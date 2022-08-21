from django.shortcuts import render, HttpResponse
from home.models import Contact,Register
from datetime import datetime
def index(request):
    context= {
        'variable' : "This is sent"
    }
    return render (request,'index.html', context)

def about(request):
    return render (request,'about.html')
    #return HttpResponse("This is about page")

def services(request):
   return render (request,'services.html')
   #return HttpResponse("This is services page")

def contact(request):
    if request.method == "POST":
     name=request.POST.get('name')
     email=request.POST.get('email')
     phone=request.POST.get('phone')
     desc=request.POST.get('desc')
     contact=Contact(name=name, email=email, phone=phone, desc=desc, date= datetime.today())
     contact.save()
    return render (request,'contact.html')
    #return HttpResponse("This is contact page")
def register(request):
    if request.method == "POST":
     name=request.POST.get('name')
     roll=request.POST.get('roll')
     year=request.POST.get('year')
     email=request.POST.get('email')
     phone=request.POST.get('phone')
     register=Register(name=name, roll=roll,year=year, email=email, phone=phone, date=datetime.today())
     register.save()
    return render (request,'register.html')
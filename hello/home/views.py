from django.shortcuts import render, HttpResponse
from home.models import Contact,Register
from datetime import datetime
from home.models import AlumniStory
from home.models import Story
from home.models import ViewStory
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

def Alumni_Stories(request):
    storys=AlumniStory.objects.all()
    ctx = {'storys':storys}
    return render(request,'stories.html',ctx)

def ReadStory (request, story_id):
    if story_id:
        try:
            read_story = Story.objects.get(id=story_id)
            print(read_story)
            return render(request, 'read.html', { 'read_story': read_story})
        except:
            return HttpResponse('Story does not exist')
    reads = Story.objects.all()
    read_story = ViewStory.objects.get(id=story_id)
    context = {
        'reads': reads
    }
    print(reads)
    return render(request, 'read.html',context)
    
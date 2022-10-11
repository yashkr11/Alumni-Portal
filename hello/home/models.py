from django.db import models
from django.utils import timezone
class Contact(models.Model):
    name=models.CharField(max_length=130)
    email=models.CharField( max_length=254)
    phone=models.CharField(max_length=12)
    desc= models.TextField()
    date= models.DateField()
    def __str__(self):
      return self.name

class Register(models.Model):
     name=models.CharField(max_length=130)
     roll=models.CharField(max_length=130)
     year=models.CharField(max_length=30)
     email=models.CharField(max_length=254)
     phone=models.CharField(max_length=12)
     date= models.DateField()
     def __str__(self):
      return self.name
class Event(models.Model):
    event_name=models.CharField(max_length=50)
    start_date=models.DateField()
    start_time=models.TimeField()
    finish_date=models.DateField()
    finish_time=models.TimeField()
    event_city=models.CharField(max_length=40)
    class Meta:
            verbose_name = 'Event'
            verbose_name_plural = 'Events'
    def __str__(self):
        return self.event_name       


class Info(models.Model):
    name=models.CharField(max_length=50)
    branch=models.CharField(max_length=50)
    email=models.EmailField()
    current_city=models.CharField(max_length=50)
    yog=models.CharField(max_length=10)
    contact=models.CharField(max_length=12)
    password=models.CharField(max_length=50)
    status=models.TextField(max_length=400)
    rollnum=models.CharField(max_length=15 , primary_key='true')
    class Meta:
        verbose_name='Info'
        verbose_name_plural='Info'
    def __str__(self):
        return self.name    

class Story(models.Model):
    uploadedBy=models.CharField(max_length=15,verbose_name='Name')
    story_name=models.CharField(max_length=50)
    story=models.CharField(max_length=1000)
    
    class Meta:
        verbose_name='Story'
        verbose_name_plural='Stories'
    def __str__(self):
        return self.story_name  

class AlumniStory(models.Model):
    UploadTime=models.DateField()
    StoryTitle=models.CharField(max_length=50)
    StoryDescp=models.TextField(max_length=150)
    StoryImage=models.ImageField(null=True , blank=True ,upload_to="images/")
    class Meta:
        verbose_name='AlumniStory'
        verbose_name_plural='AlumniStories'
    def __str__(self):
        return self.StoryTitle    

class ViewStory(models.Model):
    story_title=models.ForeignKey(AlumniStory, on_delete=models.CASCADE)
    content=models.ForeignKey(Story, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name='ViewStory'
        verbose_name_plural='ViewStories'


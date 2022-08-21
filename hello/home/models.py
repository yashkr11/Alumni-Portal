from django.db import models
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


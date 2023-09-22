from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=25)
    email=models.EmailField()
    subject=models.CharField(max_length=120)
    message=models.TextField()
    
    def __str__(self):
        return self.name


class Service(models.Model):
    
    image=models.ImageField(upload_to='blog',blank=True,null=True)
    

  
    
class Blogs(models.Model):
    title=models.CharField(max_length=60)
    description=models.TextField()
    authname=models.CharField(max_length=15)
    img=models.ImageField(upload_to='blog',blank=True,null=True)
    timeStamp=models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return self.title


class Portfolio(models.Model):
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50,default="")
    subcategory = models.CharField(max_length=50,default="")
    dese= models.CharField(max_length=300)
    image = models.ImageField(upload_to='blog',blank=True,null=True)

    def __str__(self):
        return self.product_name
    

class Task(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    skills = models.TextField(max_length=1000)
    previous_work = models.TextField(max_length=1000)
    
    
    def __str__(self):
        return self.name
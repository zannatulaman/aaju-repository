from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=25)
    email=models.EmailField()
    phonenumber=models.CharField(max_length=10)
    description=models.TextField()
    
    
class Blogs(models.Model):
    title=models.CharField(max_length=60)
    description=models.TextField()
    authname=models.CharField(max_length=15)
    img=models.ImageField(upload_to='blog',blank=True,null=True)
    timeStamp=models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return self.title

class Internship(models.Model):
    fullname=models.CharField(max_length=60)
    usn=models.CharField(max_length=60)
    email=models.CharField(max_length=60)
    college_name=models.CharField(max_length=100)
    offer_status=models.CharField(max_length=60)
    start_date=models.CharField(max_length=60)
    end_date=models.CharField(max_length=60)
    proj_report=models.CharField(max_length=60)
    timeStamp=models.DateTimeField(auto_now_add=True,blank=True)
    def __str__(self):
        return self.usn


class About(models.Model):
    birthday=models.CharField(max_length=60)
    phonenumber=models.CharField(max_length=60)
    website=models.CharField(max_length=100)
    age=models.CharField(max_length=10)
    city=models.CharField(max_length=50)
    phoneEmail=models.CharField(max_length=100)
    freelance=models.CharField(max_length=50)
    degree=models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.birthday
    

class Portfolio(models.Model):
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50,default="")
    subcategory = models.CharField(max_length=50,default="")
    dese= models.CharField(max_length=300)
    image = models.ImageField(upload_to='blog',blank=True,null=True)

    def __str__(self):
        return self.product_name


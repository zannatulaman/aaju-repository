from django.shortcuts import render,redirect
from django.contrib import messages
from portfolio.models import Contact,Blogs,Portfolio,Service,Task
from django.http import HttpResponse
from django.template import loader
import pdfkit
import io

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):

    return render(request,'about.html')

def mywork(request):
    posts=Portfolio.objects.all()
    context={"posts":posts}
    return render(request,'mywork.html',context)

def skills(request):
    posts=Blogs.objects.all()
    context={"posts":posts}
    return render(request,'skills.html',context)
    
def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject =request.POST.get('subject')
        message=request.POST.get('message')
        query=Contact(name=name,email=email,subject=subject,message=message)
        query.save()
        messages.success(request,"Thanks for contacting us. We will get by you Soon!")

        return redirect('/')
    return render(request,'contact.html')

def basic(request):
    return render(request,'basic.html')


def services(request):
    posts=Service.objects.all()
    context={"posts":posts}
    return render(request,'services.html',context)

def accept(request):
    if request.method=="POST":
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        school=request.POST.get('school')
        degree=request.POST.get('degree')
        university=request.POST.get('university')
        skills=request.POST.get('skills')
        previous_work=request.POST.get('previous_work')
        
        query=Task(name=name,phone=phone,email=email,school=school,degree=degree,university=university,skills=skills,previous_work=previous_work)
        query.save()   
    return render(request,'accept.html')

def resume(request,id):
    user_profile = Task.objects.get(pk=id)
    template = loader.get_template("resume.html")
    html = template.render({'user_profile':user_profile})
    option={
        'page-size':'Letter',
        'encoding':'UTF-8'
        }
    pdf = pdfkit.from_string(html,False,option)
    response = HttpResponse(pdf,cotent_type='application/pdf')
    response['Content-Disposition']='attachment'
    return response
    
    
    

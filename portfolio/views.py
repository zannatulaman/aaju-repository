from django.shortcuts import render,redirect
from django.contrib import messages
from portfolio.models import Contact,Blogs,Internship,About,Portfolio

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    if request.method=="POST":
        bday=request.POST.get('birth')
        pEmail=request.POST.get('email')
        phonenum=request.POST.get('num')
        website=request.POST.get('web')
        age=request.POST.get('age')
        city=request.POST.get('city')
        freelance=request.POST.get('free')
        degree=request.POST.get('deg')
        
        query=About(birthday=bday,phoneEmail=pEmail,phonenumber=phonenum,website=website,age=age,city=city,freelance=freelance,degree=degree)
        query.save()
        
        return redirect('/')
    return render(request,'about.html')

def portfolio(request):
    posts=Portfolio.objects.all()
    context={"posts":posts}
    return render(request,'portfolio.html',context)

def handleblog(request):
    posts=Blogs.objects.all()
    context={"posts":posts}
    return render(request,'handleblog.html',context)

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phonenum=request.POST.get('num')
        desc=request.POST.get('desc')
        query=Contact(name=name,email=email,phonenumber=phonenum,description=desc)
        query.save()
        messages.success(request,"Thanks for contacting us. We will get by you Soon!")

        return redirect('/auth/login/')
    return render(request,'contact.html')

def basic(request):
    return render(request,'basic.html')

def internshipdetails(request):
    # if not request.user.is_authenticated:
    #     messages.warning(request,"Please login to access this page")
    #     return redirect("/auth/login/")

    if request.method=="POST":
        fname=request.POST.get('name')
        femail=request.POST.get('email')
        fusn=request.POST.get('usn')
        fcollege=request.POST.get('cname')
        foffer=request.POST.get('offer')
        fstartdate=request.POST.get('startdate')
        fenddate=request.POST.get('enddate')
        fprojreport=request.POST.get('projreport')

# converting to upper case
        fname=fname.upper()
        fusn=fusn.upper()
        fcollege=fcollege.upper()
        fprojreport=fprojreport.upper()
        foffer=foffer.upper()

        # 
        check1=Internship.objects.filter(usn=fusn)
        check2=Internship.objects.filter(email=femail)

        if check1 or check2:
            messages.warning(request,"Your Details are Stored Already")
            
        query=Internship(fullname=fname,usn=fusn,email=femail,college_name=fcollege,offer_status=foffer,start_date=fstartdate,end_date=fenddate,proj_report=fprojreport)
        query.save()

        messages.success(request,"Form is Submitted Successful!")
        return redirect('/internshipdetails/')
    return render(request,'intern.html')


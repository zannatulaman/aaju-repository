from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate,login, logout

# Create your views here.
def signup(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        if password1!= password2:
            return HttpResponse('Your password and confirm password are not same')
        my_user= User.objects.create_user(username,email,password1)
        my_user.save()
        return redirect('/auth/login/')
    
    return render(request,'signup.html')

def user_login(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            return HttpResponse('User or password in incorrect')
    
        
    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('/auth/login/')
    return render(request, 'logout.html')
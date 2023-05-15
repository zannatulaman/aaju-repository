from django.urls import path
from portfolio import views
urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('portfolio/',views.portfolio,name='portfolio'),
    path('blog/',views.handleblog,name='handleblog'),
    path('contact/',views.contact,name='contact'),
    path('basic',views.basic,name='basic'),
    path('internshipdetails/',views.internshipdetails,name='internshipdetails'),

]

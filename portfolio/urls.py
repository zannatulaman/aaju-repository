from django.urls import path
from portfolio import views
urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('mywork/',views.mywork,name='mywork'),
    path('skills/',views.skills,name='skills'),
    path('contact/',views.contact,name='contact'),
    path('basic',views.basic,name='basic'),
    path('services/',views.services,name='services'),
    path('accept',views.accept,name='accept'),
    path('<int:id>/',views.resume,name='resume'),
]


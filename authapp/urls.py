from django.urls import path
from authapp import views
urlpatterns = [
    path('auth/signup/',views.signup,name='signup'),
    path('auth/login/',views.user_login,name='login'),
    path('auth/logout/',views.user_logout,name='logout'),
]
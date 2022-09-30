from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_page,name='homepage'),
    path('login',views.login_page,name='login'),
    path('signup',views.signup_page,name='signup'),

    
]

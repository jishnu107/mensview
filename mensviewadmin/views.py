from django.shortcuts import render

# Create your views here.

def home_page(request):
    return render(request,'mensviewadmin/homepage.html')
def login_page(request):
    return render(request,'mensviewadmin/login.html')

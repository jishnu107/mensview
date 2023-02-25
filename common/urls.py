from django.urls import path
from . import views

app_name = 'common'
urlpatterns = [
    path('commonhome',views.commonhome_page,name='common'),
    path('custreg',views.custreg_page,name='custreg'),
    path('sellreg',views.sellreg_page,name='sellreg'),
    path('selllogin',views.selllogin_page,name='selllogin'),
    path('custlogin',views.custlogin_page,name='custlogin'),
    path('allview',views.allview_page,name='allview'), 
    # path('details',views.productdetails_page,name='detailspage'),    

]
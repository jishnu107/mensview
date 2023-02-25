from django.urls import path
from . import views

app_name = 'seller'
urlpatterns = [
    path('home',views.home_page,name='homepage'),
    path('orders',views.orders_page,name='orders'), 
    path('product',views.product_page,name='product'),    
    path('addprod',views.addprod_page,name='addprod'), 
    path('updateprod',views.updateprod_page,name='updateprod'), 
    path('sprofile',views.sprofile_page,name='sprofile'), 
    path('pdetails/<int:pid>',views.pdetails_page,name='pdetails'),
    path('logout',views.logout,name='logout'),
    path('getstock', views.get_stock, name='getstock'),
    path('trend/<int:pid>',views.trend,name='trend'),
    path('untrend/<int:pid>',views.un_trend,name='untrend'),
    path('deleteprod/<int:sid>',views.delete_prod,name='deleteprod'),
]
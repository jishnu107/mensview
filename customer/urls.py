from django.urls import path
from . import views

app_name = 'customer'
urlpatterns = [
    path('home',views.home_page,name='homepage'), 
    path('details/<int:pid>',views.productdetails_page,name='detailspage'),    
    path('cart',views.cart_page,name='cartpage'), 
    path('wishlist',views.wishlist_page,name='wishlist'), 
    path('profile',views.profile_page,name='profile'), 
    path('allview',views.allview_page,name='allview'),
    path('category',views.category_page,name='category'), 
    path('category/<str:data>',views.category_page,name='categorywise'), 
    path('remove_cart/<int:pid>',views.remove_item,name='remove_cart'),
    path('remove_wish/<int:pid>',views.removewish_item,name='remove_wish'),
    path('logout',views.logout,name='logout'),
    path('addwishlist/<int:pid>',views.add_to_wishlist, name="addwishlist")
]
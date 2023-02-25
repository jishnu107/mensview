from django.shortcuts import render,redirect
from common.models import Customer,Seller
from seller.models import Product
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def adminhome_page(request):
    customers = Customer.objects.all()
    product_list = Product.objects.all()
    sellers = Seller.objects.filter(approved=True)
    context = {
        'customer_list':customers,
        'seller_list':sellers,
        'prods': product_list
    }
    return render(request,'mensviewadmin/adminhome.html',context)
def approve_page(request):
    sellers = Seller.objects.filter(approved = False)
    return render(request,'mensviewadmin/approve.html',{'seller_app':sellers})
def viewsellers_page(request):
    sellers = Seller.objects.filter(approved=True)
    return render(request,'mensviewadmin/viewsellers.html',{'seller_list':sellers})
def viewcust_page(request):
    customers = Customer.objects.all()
    context = {
        'customer_list':customers
    }
    return render(request,'mensviewadmin/viewcust.html',context)
def viewprod_page(request):
    product_list = Product.objects.all()
    seller_data = Seller.objects.all()
    context =  {'prods': product_list,
                'data': seller_data,
                }
    return render(request,'mensviewadmin/viewprod.html',context)
def approve(request,sid):
    seller=Seller.objects.get(id=sid)
    seller.approved=True
    seller.save()
    return redirect('mensviewadmin:viewsellers')
def delete_seller(request,sid):
    seller_list = Seller.objects.get(id = sid)
    seller_list.delete()
    return redirect('mensviewadmin:sellerview')
def delete_cust(request,sid):
    cust_list = Customer.objects.get(id = sid)
    cust_list.delete()
    return redirect('mensviewadmin:viewcust')
def delete_prod(request,sid):
    prod_list = Product.objects.get(id = sid)
    prod_list.delete()
    return redirect('mensviewadmin:viewprod')

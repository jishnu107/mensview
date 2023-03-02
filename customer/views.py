from django.shortcuts import render,redirect
from seller.models import Product
from common.models import Customer,Seller
from .models import Cart,Wishlist
from .auth_gaurd import auth_customer
from django.db.models import Q

# from .models import Cart

# Create your views here.
@auth_customer
def master_page(request):   
    return render(request,'customer/master.html')
@auth_customer
def home_page(request):
    product_list = Product.objects.filter(trend = True)
    context ={'prods': product_list,
            }
    return render(request,'customer/homepage.html',context)
@auth_customer
def productdetails_page(request,pid):
    msg=''
    products_details = Product.objects.get(id = pid)
    if request.method == 'POST':
        product_size = request.POST['p_size']
        product_exist = Cart.objects.filter(product = pid,customer = request.session['customer'] ).exists()
        if not product_exist:
            cart = Cart(customer_id = request.session['customer'],product_id = pid)
            cart.product_size = product_size
            cart.save()
            msg = 'Item added to cart'
        else:
            msg = 'Item already in cart'
    context ={'details':products_details,
                'msg':msg
                }
    return render(request,'customer/viewproduct.html',context)
@auth_customer
def cart_page(request):
    product_cart = Cart.objects.filter(customer = request.session['customer'])
    return render(request,'customer/cart.html',{'cart_list':product_cart})
@auth_customer
def profile_page(request):
    msg=''
    cust_list = Customer.objects.get(id=request.session['customer'])
    if request.method=='POST':
        customer = Customer.objects.get(id = request.session['customer'])

        customer_name = request.POST['c_name']
        email_address = request.POST['c_email']
        address = request.POST['c_address']
        phone_number = request.POST['c_number']

        customer.customer_name = customer_name
        customer.email_address = email_address
        customer.address = address
        customer.phone_number = phone_number
        customer.save()
        msg = 'Profile updated successfully'
    context = {
        'custs': cust_list,
        'msg':msg
    }
    return render(request,'customer/profile.html',context)
@auth_customer
def allview_page(request):
    product_list = Product.objects.all()
    return render(request,'customer/allview.html',{'prods': product_list})
@auth_customer
def category_page(request, data=None):
    if data == None:
        products = Product.objects.all()
    elif data == 'Shirt' or data == 'T-shirt' or data == 'Pant' or data == 'Accessories' or data == 'Shoes' or data == 'Casuals' or data == 'Innerwears':
        products = Product.objects.filter(product_cat=data) 
    return render(request,'customer/category.html',{'prods': products})
def remove_item(request,pid):
    cart_item = Cart.objects.get(product = pid,customer = request.session['customer'])
    cart_item.delete()
    return redirect('customer:cartpage')
def logout(request):
    del request.session['customer'] 
    request.session.flush()
    return redirect('common:custlogin')
@auth_customer
def wishlist_page(request):
    product_wishlist = Wishlist.objects.filter(customer = request.session['customer'])
    return render(request,'customer/wishlist.html',{'wish_list':product_wishlist})
def add_to_wishlist(request,pid):
    product_exist = Wishlist.objects.filter(product = pid,customer = request.session['customer'] ).exists()
    if not product_exist:
        wishlist = Wishlist(customer_id = request.session['customer'],product_id = pid)
        wishlist.save()
        return redirect('customer:allview')

    else:
        return redirect('customer:wishlist')
def removewish_item(request,pid):
    wishlist_item = Wishlist.objects.get(product = pid,customer = request.session['customer'])
    wishlist_item.delete()
    return redirect('customer:wishlist')
def checkout_page(request):
    product_cart = Cart.objects.filter(customer = request.session['customer'])
    return render(request,'customer/checkout.html',{'cart_list':product_cart})
def search_page(request): 
    if request.method=='POST': 
        search_word = request.POST['searchdata'] 
        searchproducts = Product.objects.filter(Q(product_name__icontains = search_word) |  
                                                Q(product_description__icontains = search_word) |                                                 
                                                Q(price__icontains = search_word) | 
                                                Q(product_cat__icontains = search_word),) 
        return render(request,'customer/searchprod.html',{'searchprod':searchproducts}) 
    else:
        return redirect('customer/search')

def pass_page(request):
    msg =''
    cust_data = Customer.objects.get(id=request.session['customer'])
    if request.method == 'POST':
        customer = Customer.objects.get(id = request.session['customer'])

        current_pass = request.POST['current_pass'] 
        new_pass = request.POST['new_pass'] 
        confirm_pass = request.POST['confirm_pass']

        if customer.cust_password == current_pass:

            if new_pass == confirm_pass:
                 customer.cust_password = new_pass
                 customer.save()
                 msg = 'Password changed succesfully'

            else:
                msg = 'Password does not match'

        else:
            msg = 'Incorrect Password'
    context =  {'msg':msg,
                'data': cust_data,
                }
    return render(request, 'customer/pass.html',context)
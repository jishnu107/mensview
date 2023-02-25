from django.shortcuts import render,redirect
from seller.models import Product
from common.models import Customer,Seller
from .models import Cart,Wishlist

# from .models import Cart

# Create your views here.
def home_page(request):
    product_list = Product.objects.filter(trend = True)
    context ={'prods': product_list,
            }
    return render(request,'customer/homepage.html',context)
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
def cart_page(request):
    product_cart = Cart.objects.filter(customer = request.session['customer'])
    return render(request,'customer/cart.html',{'cart_list':product_cart})
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
def allview_page(request):
    product_list = Product.objects.all()
    return render(request,'customer/allview.html',{'prods': product_list})
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
    
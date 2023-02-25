from django.shortcuts import render,redirect
from . models import Customer,Seller
import random

# Create your views here.
from django.shortcuts import render

# Create your views here.
def commonhome_page(request):
    return render(request,'common/commonhome.html')
def custreg_page(request):
    if request.method == 'POST':
        c_name = request.POST['c_name']
        c_email = request.POST['c_email']
        c_address = request.POST['c_address']
        c_number = request.POST['c_number']
        c_gender = request.POST['c_gender']
        c_password = request.POST['c_password']
        new_customer = Customer(customer_name = c_name , email_address = c_email,address = c_address,phone_number = c_number,gender= c_gender,cust_password=c_password)
        new_customer.save()
        return redirect('common:custlogin')
    return render(request,'common/custreg.html')
def sellreg_page(request):
    if request.method == 'POST':
        seller_name = request.POST['s_name']
        seller_email = request.POST['s_email']
        seller_address = request.POST['s_address']
        seller_number = request.POST['s_phone']
        gender = request.POST['s_gen']
        company_name = request.POST['comp_name']
        accholder = request.POST['accholder_name']
        branch = request.POST['s_branch']
        ifsc = request.POST['s_ifsc']
        seller_image = request.FILES['s_image']
        acc_number = request.POST['accnum']
        seller_pass = request.POST['s_password']

        seller_list = Seller(seller_name = seller_name,seller_email = seller_email,address = seller_address,phone_number = seller_number, 
                      gender = gender,comp_name = company_name,accholder_name = accholder, ifsc = ifsc,  branch = branch, acc_number=acc_number,
                      sell_pic = seller_image,seller_pass = seller_pass)
        seller_list.save()
        return redirect('common:selllogin')

    return render(request,'common/sellreg.html')
def selllogin_page(request):
    msg = ''
    if request.method == 'POST':
        sell_email = request.POST['s_email'] 
        sell_password = request.POST['sell_password']

        try :
            seller = Seller.objects.get(seller_email = sell_email, seller_pass = sell_password,approved = True)
            request.session['seller'] = seller.id
            return redirect('seller:homepage')
        except:
            
             msg = 'email or password incorrect'

    return render(request,'common/selllogin.html',{'msg':msg})
def custlogin_page(request):
    custmsg = ''
    if request.method == 'POST':
        cust_email = request.POST['c_email'] 
        cust_password = request.POST['cust_password'] 

        try :
            customer = Customer.objects.get(email_address = cust_email, cust_password = cust_password ) 
            request.session['customer'] = customer.id
            return redirect('customer:homepage')
        except:
            custmsg = 'username or password incorrect'  

    return render(request,'common/custlogin.html',{'custmsg':custmsg})
def allview_page(request):
    return render(request,'common/allview.html')
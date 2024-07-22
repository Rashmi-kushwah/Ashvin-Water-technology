from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.conf import settings
import requests as r
from django.core.mail import send_mail
from django.utils.crypto import get_random_string

from django.contrib.auth import get_user_model
from django.urls import reverse
User = get_user_model()
from django.contrib.auth.models import User
from Cart.models import addcart
from Admin .models import admin_user

from User.models import Eurekaforbes_User
from Product.models import *
from Orders.models import Order

from django.shortcuts import render, get_object_or_404
 
from django.shortcuts import render, redirect
from django.http import HttpResponse
import uuid
from datetime import datetime
from Galleryapp.models import Page
from django.views.decorators.csrf import csrf_exempt

###################################### LOGIN   METHOD ################################################


# @csrf_exempt
# def user_login(request):
#     if request.session.get('user_uid'):
#         return redirect('/')  

#     msg = request.GET.get('message', None)

#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         remember_me = request.POST.get('remember_me')

#         try:
#             user = Eurekaforbes_User.objects.get(email=email)
#             if password == user.password:
#                 request.session['user_uid'] = str(user.user_uid)
#                 if remember_me:
#                     request.session.set_expiry(2592000)  # 30 days in seconds
#                 else:
#                     request.session.set_expiry(0)

#                 return redirect('/')
#             else:
#                 return render(request, 'login.html', {'error': 'Invalid password'})
#         except Eurekaforbes_User.DoesNotExist:
#             return render(request, 'login.html', {'error': 'Email id is not registered'})

#     return render(request, 'login.html', {'error': msg})

from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect


@csrf_protect
def user_login(request):
    if request.session.get('user_uid'):
        return redirect('/')  # Redirect to homepage if already logged in

    msg = request.GET.get('message', None)

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        remember_me = request.POST.get('remember_me')

        try:
            user = Eurekaforbes_User.objects.get(email=email)
            if password == user.password:
                request.session['user_uid'] = str(user.user_uid)
                request.session.set_expiry(2592000 if remember_me else 0)  # 30 days or browser session

                return redirect('/')
            else:
                return render(request, 'login.html', {'error': 'Invalid password'})
        except Eurekaforbes_User.DoesNotExist:
            return render(request, 'login.html', {'error': 'Email id is not registered'})

    return render(request, 'login.html', {'error': msg})

###################################### REGISTER   METHOD ################################################

def register(request):
    error = ''
    if request.method == 'POST':
        name = request.POST.get('name')
        phone_number = request.POST.get('mo')
        email = request.POST.get('email')
        password = request.POST.get('pass')
        
        try:
          
            user = Eurekaforbes_User.objects.get(email=email)
       
            return render(request, 'register.html', {'error': 'Email address already registered.'})
        
        except Eurekaforbes_User.DoesNotExist:
          
            otp = get_random_string(length=6, allowed_chars='1234567890')
            request.session['email'] = email

            subject = 'Your OTP for Eurekaforbes'
            message = f'Thank you for using Eurekaforbes! To complete your login, please use the One-Time Password (OTP) provided below: OTP: {otp}'
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [email]
            
            try:
                send_mail(subject, message, from_email, recipient_list)
                
                
                user = Eurekaforbes_User(
                    email=email,
                    otp=otp,
                    password=password ,
                    name=name,
                    phone_number=phone_number,
        
                )
                user.save()
                
              
                return redirect('/otp/verify/')
            
            except Exception as e:
                error = str(e)
                return render(request, 'register.html', {'error': error})
    
    else:
        return render(request, 'register.html', {'error': error})



###################################### REGISTER  OTP METHOD ################################################

def send_otp_email(email):
    otp = get_random_string(length=6, allowed_chars='1234567890')
    subject = 'Your OTP for eurekaforbes'
    message = f'Your OTP is: {otp}'
    from_email = 'rashmiinfo6@gmail.com' 
    recipient_list = [email]
    
    send_mail(subject, message, from_email, recipient_list)
    print('send email ')
    
    return otp

def otp_verify(request):
    if request.method == 'POST':
        otp = request.POST.get('otp')
        print('otp',otp)
        email = request.session.get('email')
        print(email)
        user = Eurekaforbes_User.objects.get(email=email)
        if otp == user.otp: 
            return redirect(reverse('login') + '?message=verification successful') 
     
        else:
            return render(request,'otp page.html',{'error': 'invalid otp'})    

    return render(request,'otp page.html')    


from django.shortcuts import render, redirect
from django.contrib import messages



###################################### REGISTER  OTP METHOD ################################################
######################################  OTP METHOD ############################################################


def otp(request):
    try:
        user_id = request.session.get('user_uid')
        user = Eurekaforbes_User.objects.get(user_uid=user_id)
       
        return render(request,"otp page.html")

    except:
     return redirect('/login/?message=Please login') 
    



###################################### FORGOT   METHOD ################################################

import random
def forgot_password(request):
    if request.method == 'POST': 
            email = request.POST.get('email')
            if Eurekaforbes_User.objects.filter(email=email):
                try:    
                    code = ''.join([str(random.randint(0, 9)) for _ in range(6)])
                    ad = Eurekaforbes_User.objects.get(email=email)
                    ad.verify_code = code
                    ad.save()
                    subject = 'Hello send verify code!'
                    message=f'please use the One-Time Password (OTP) provided below:Verification code is: {code}'
                 
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list = [email]  
                    send_mail(subject, message, email_from, recipient_list)
                    print(code)
                    print('send mail')
                   
                    otp_url = reverse('Otp_view') + f'?email={email}'
                    return redirect(otp_url)
                
                except:
                    return render(request, 'forgot_password.html' , {'error':'Not send verify code'}) 
            else:
                return render(request, 'forgot_password.html' , {'error':'Email is not registered'})  
    return render(request, 'forgot_password.html' )

###################################### FORGET  OTP METHOD ################################################

def otp_view(request):
    email = request.GET.get('email')
    user = Eurekaforbes_User.objects.get(email=email)
    if request.method == 'POST': 
        code = request.POST.get('verify_code')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        print(email, code, pass1, pass2)
        remember_me = request.POST.get('remember_me')
        if user.verify_code == code and pass1 == pass2:
            user.password = pass1
            user.save()
            if remember_me:
                request.session.set_expiry(2592000)  
                print(remember_me, 'remember_me')
            else:
                request.session.set_expiry(0)
                print('remember me')
                
            return redirect('/login?msg=Your password is reset, please sign in')
        
        
        else:
            return render(request, 'otp_view.html', {'msg': 'Something went wrong'})
    return render(request, 'otp_view.html')

######################################  METHOD ##########################################################

######################################  CATEGORY  METHOD START ###########################################

def main_Category(request):
    try:
        user_id = request.session.get('user_uid')
        user = Eurekaforbes_User.objects.get(user_uid=user_id)
        return Main_Category.objects.all()
   
    except:
     return redirect('/login/?message=Please login')     


 

def sub_category(request):
    try:
        user_id = request.session.get('user_uid')
        user = Eurekaforbes_User.objects.get(user_uid=user_id)
        
        return Sub_Category.objects.all()

    except:
     return redirect('/login/?message=Please login')     
 
######################################  HOMEPAGE  METHOD START ##################################################
def home(request):
    user_id = request.session.get('user_uid')
    if not user_id:
        return redirect('/login/?message=Please login')

    try:
        user = Eurekaforbes_User.objects.get(user_uid=user_id)
        cart_product = addcart.objects.filter(user_uid=user_id)
        cart_count = cart_product.count()
        pages = Page.objects.all()
        print(main_Category(request))
        print(sub_category(request))
        water_purifier_category = Main_Category.objects.get(main_Categorytype='Water Purifier')
        
        # Filter products based on order_status and main category
        all_products = Product.objects.filter(order_status='Trending', main_category=water_purifier_category)[:3]
        data = {
            'product': all_products,
            'pages': pages,
            'cart_count': cart_count,
            'main_Category': main_Category(request),
            'sub_category': sub_category(request)
        }

        return render(request, 'Homepage.html', data)
    except Eurekaforbes_User.DoesNotExist:
        return redirect('/login/?message=User not found')


######################################  HOMEPAGE  METHOD CLOSE ######################################################

###################################### PRODUCT METHOD  START ################################################
def PRODUCT(request):
    try:
        user_id = request.session.get('user_uid')
        user = Eurekaforbes_User.objects.get(user_uid=user_id)

        
        all_products = Product.objects.filter(active_product=True)
        print('Allproduct', all_products)

        cart_product = addcart.objects.filter(user_uid=user_id)
        cart_count = cart_product.count()
        
        data = {
            'product': all_products,
            'cart_count': cart_count,
            'main_Category': main_Category(request),
            'sub_category': sub_category(request)
        }
        return render(request, 'Product.html', data)
    
    except Eurekaforbes_User.DoesNotExist:
        return redirect('/login/?message=Please login')

    
def New_Launchproduct(request):
    try:
        user_id = request.session.get('user_uid')
        user = Eurekaforbes_User.objects.get(user_uid=user_id)
        all_products = Product.objects.filter(order_status='New')
        print('Allproduct', all_products)
        cart_product = addcart.objects.filter(user_uid=user_id)
        cart_count = cart_product.count()
        data = {
            'product': all_products,
            'cart_count': cart_count,
            'main_Category': main_Category(request),
            'sub_category': sub_category(request)
        }
        
        return render(request, 'Product.html', data)
    except Eurekaforbes_User.DoesNotExist:
        return redirect('/login/?message=Please login')

def Trending_Launchproduct(request):
    try:
        user_id = request.session.get('user_uid')
        user = Eurekaforbes_User.objects.get(user_uid=user_id)
        
        water_purifier_category = Main_Category.objects.get(main_Categorytype='Water Purifier')
        
        # Filter products based on order_status and main category
        all_products = Product.objects.filter(order_status='Trending', main_category=water_purifier_category)[:3]
        print('Allproduct', all_products)
        
        cart_product = addcart.objects.filter(user_uid=user_id)
        cart_count = cart_product.count()
        
        data = {
            'product': all_products,
            'cart_count': cart_count,
            'main_Category': main_Category(request),
            'sub_category': sub_category(request)
        }
        
        return render(request, 'Homepage.html', data)

    except Eurekaforbes_User.DoesNotExist:
        return redirect('/login/?message=Please login')

######################################  PRODUCT METHOD  CLOSE ################################################

###################################### PRODUCT  DETAIL METHOD  START #########################################

def Product_Detail(request,Pd_id):
    try:
        user_id = request.session.get('user_uid')
        user = Eurekaforbes_User.objects.get(user_uid=user_id)
        get_product = Product.objects.filter(Product_id=Pd_id)
        print('get_product',get_product)

        cart_product = addcart.objects.filter(user_uid=user_id)
        cart_count = cart_product.count()
        print(cart_count )

    
        data={
            'get_product': get_product, 
            'cart_count': cart_count,
            # 'product': all_products,
            'main_Category':main_Category(request),
            'sub_category':sub_category(request)
        }

        return render(request, 'product detailpage.html',data)
    
    except:
     return redirect('/login/?message=Please login') 
    
###################################### PRODUCT METHOD  CLOSE ################################################

######################################   PROFILE  METHOD START ##############################################

def profile(request):
    try:
        user_id = request.session.get('user_uid')
        user = Eurekaforbes_User.objects.get(user_uid=user_id)
    
        cart_product = addcart.objects.filter(user_uid=user_id)
        cart_count = cart_product.count()

        user_data = Eurekaforbes_User.objects.filter(user_uid=user_id)


        all_orders = Order.objects.filter(user_uid=user_id).order_by('-id')
        all_orders_count = all_orders.count()
        shipped_orders = Order.objects.filter(user_uid=user_id, order_status='shipped').order_by('-id')
        shipped_orders_count = shipped_orders.count()
        new_orders = Order.objects.filter(user_uid=user_id, order_status='New').order_by('-id')
        new_orders_count = new_orders.count()
        delivered_orders = Order.objects.filter(user_uid=user_id, order_status='delivered').order_by('-id')
        delivered_orders_count = delivered_orders.count()
        ready_orders = Order.objects.filter(user_uid=user_id, order_status='ready').order_by('-id')
        ready_orders_count = ready_orders.count()
        canceled_orders = Order.objects.filter(user_uid=user_id, order_status='canceled').order_by('-id')
        canceled_orders_count = canceled_orders.count()

        data={
            'user_data':user_data,
            'cart_count': cart_count,
              'main_Category':main_Category(request),
            'sub_category':sub_category(request),

            'all_orders_count': all_orders_count,
            'shipped_orders_count': shipped_orders_count,
            'new_orders_count': new_orders_count,
            'delivered_orders_count': delivered_orders_count,
            'ready_orders_count': ready_orders_count,
            'canceled_orders_count': canceled_orders_count,
            
              

        }

        return render(request,'Profile.html',data)
    except:
     return redirect('/login/?message=Please login')    





# ####################################################################################################################

def user_all_order(request):
    try:
        user_id = request.session.get('user_uid')
        all_orders = Order.objects.filter(user_uid=user_id).order_by('-id')
        all_orders_count = all_orders.count()
        
        cart_product = addcart.objects.filter(user_uid=user_id)
        cart_count = cart_product.count()
        
        data = {
            'orders': all_orders,
            'all_orders_count': all_orders_count,
            'cart_count': cart_count,
              'main_Category':main_Category(request),
            'sub_category':sub_category(request)
        }
        
        return render(request, 'order.html', data)
    except:
     return redirect('/login/?message=Please login') 

def user_shipped_order(request):
    try:

        user_id = request.session.get('user_uid')
        shipped_orders = Order.objects.filter(user_uid=user_id, order_status='shipped').order_by('-id')
        shipped_orders_count = shipped_orders.count()
        
        cart_product = addcart.objects.filter(user_uid=user_id)
        cart_count = cart_product.count()
        
        data = {
            'orders': shipped_orders,
            'shipped_orders_count': shipped_orders_count,
            'cart_count': cart_count,
              'main_Category':main_Category(request),
            'sub_category':sub_category(request)
        }
        
        return render(request, 'order.html', data)
    except:
     return redirect('/login/?message=Please login') 

def user_new_order(request):
    try:
        user_id = request.session.get('user_uid')
        new_orders = Order.objects.filter(user_uid=user_id, order_status='New').order_by('-id')
    
        new_orders_count = new_orders.count()
        
        cart_product = addcart.objects.filter(user_uid=user_id)
        cart_count = cart_product.count()
        
        data = {
            'orders': new_orders,
            'new_orders_count': new_orders_count,
            'cart_count': cart_count,
              'main_Category':main_Category(request),
            'sub_category':sub_category(request)
        }
        
        return render(request, 'order.html', data)
    except:
     return redirect('/login/?message=Please login') 

def user_delivered_order(request):
    try:
        user_id = request.session.get('user_uid')
        delivered_orders = Order.objects.filter(user_uid=user_id, order_status='delivered').order_by('-id')
        delivered_orders_count = delivered_orders.count()
        
        cart_product = addcart.objects.filter(user_uid=user_id)
        cart_count = cart_product.count()
        
        data = {
            'orders': delivered_orders,
            'delivered_orders_count': delivered_orders_count,
            'cart_count': cart_count,
              'main_Category':main_Category(request),
            'sub_category':sub_category(request)
        }
        
        return render(request, 'order.html', data)
    except:
     return redirect('/login/?message=Please login') 
    

def user_ready_order(request):
    try:
        user_id = request.session.get('user_uid')
        ready_orders = Order.objects.filter(user_uid=user_id, order_status='ready').order_by('-id')
        ready_orders_count = ready_orders.count()
        
        cart_product = addcart.objects.filter(user_uid=user_id)
        cart_count = cart_product.count()
        
        data = {
            'orders': ready_orders,
            'ready_orders_count': ready_orders_count,
            'cart_count': cart_count,
              'main_Category':main_Category(request),
            'sub_category':sub_category(request)
        }
        
        return render(request, 'order.html', data)
    except:
     return redirect('/login/?message=Please login') 

def user_cancel_order(request):
    try:
        user_id = request.session.get('user_uid')
        canceled_orders = Order.objects.filter(user_uid=user_id, order_status='canceled').order_by('-id')
        canceled_orders_count = canceled_orders.count()
        
        cart_product = addcart.objects.filter(user_uid=user_id)
        cart_count = cart_product.count()
        
        data = {
            'orders': canceled_orders,
            'canceled_orders_count': canceled_orders_count,
            'cart_count': cart_count,
              'main_Category':main_Category(request),
            'sub_category':sub_category(request)
        }
        
        return render(request, 'order.html', data)
    except:
     return redirect('/login/?message=Please login') 



######################################   PROFILE  METHOD CLOSE ##############################################
  
###################################### ADDCART METHOD  START ################################################

def Adcart(request):
    try:
        user_id = request.session.get('user_uid')
        user = Eurekaforbes_User.objects.get(user_uid=user_id)

        if request.method == 'POST':
            product_id = request.POST.get('product_id')
            print("Add Product ID:", product_id)
            buy_id = request.POST.get('buy_id')
            print("Add buy ID:", buy_id)
    

            try:
                add_product_dt = Product.objects.get(Product_id=product_id)
                quantity = int(request.POST.get('quantity', 1)) 
                total_amount = quantity * add_product_dt.price
                print("Total Amount:", total_amount)

                cart = addcart(
                    Product_id=product_id,
                    user_uid=user_id,
                    sku_code=add_product_dt.sku_code,
                    title=add_product_dt.title,
                    color=add_product_dt.color,
                    img1=add_product_dt.img1,
                    price=add_product_dt.price,
                    mrp=add_product_dt.mrp,
                    qty=quantity,  
                    total_amount=total_amount,
                  
                )
                cart.save()
                messages.success(request, f"You added {add_product_dt.title} to your shopping cart.")
                return redirect('Product_Detail', Pd_id=product_id)

            except Product.DoesNotExist:
                add_buy_dt = Product.objects.get(Product_id=buy_id)
                quantity = int(request.POST.get('quantity', 1)) 
                total_amount = quantity * add_buy_dt.price
                print("Total Amount:", total_amount)

                cart = addcart(
                    Product_id=buy_id,
                    user_uid=user_id,
                    sku_code=add_buy_dt.sku_code,
                    title=add_buy_dt.title,
                    color=add_buy_dt.color,
                    img1=add_buy_dt.img1,
                    price=add_buy_dt.price,
                    mrp=add_buy_dt.mrp,
                    qty=quantity, 
                    total_amount=total_amount
                )
                cart.save()
                messages.success(request, f"You added {add_buy_dt.title} to your shopping cart.")
                return redirect('/cart/', product_id=buy_id)
            
            
    except:
     return redirect('/login/?message=Please login')   


###################################### ADDCART METHOD  CLOSE ###################################################

###################################### UPDATE CART METHOD START ################################################

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def update_cart(request):
    try:
        user_id = request.session.get('user_uid')
        print(user_id)
        user = Eurekaforbes_User.objects.get(user_uid=user_id)
        print('user', user)
        cart_product = addcart.objects.filter(user_uid=user_id)
        cart_count = cart_product.count()
        if request.method == 'POST':

            product_id = request.POST.get('product_id')
            # print('product_id',product_id)
            quantity = request.POST.get('quantity')
            # print('quantity',quantity)
            total_amount = request.POST.get('total_amount')
            print('total_amount',total_amount,product_id,quantity,'------------------------',total_amount)

            
            # product = Product.objects.get(id=product_id)
            cart_item = addcart.objects.get(id=product_id)
            cart_item.qty = quantity
            cart_item.total_amount = total_amount
            cart_item.save()

            # Response banaye aur return kare
            return JsonResponse({'success': True, 'message': 'Cart updated successfully'})
        
        return JsonResponse({'success': False, 'message': 'Invalid request'}, status=400)
    


    except:
     return redirect('/login/?message=Please login')   
###################################### UPDATE CART METHOD CLOSE ################################################

######################################  CART METHOD START ######################################################
def cart(request):
    try:
        user_id = request.session.get('user_uid')
        print(user_id)
        user = Eurekaforbes_User.objects.get(user_uid=user_id)
        print('user', user)
        cart_product = addcart.objects.filter(user_uid=user_id)
        cart_count = cart_product.count()
        if request.method == 'POST':
            user_id = request.session.get('user_uid')
            product_id = request.POST.get('product_id')
            quantity = int(request.POST.get('qty'))
            total_amount = int(request.POST.get('total_amount'))
            
            cart_item = addcart.objects.get(user_uid=user_id, Product_id=product_id)
            cart_item.qty = quantity
            cart_item.total_amount = total_amount
            cart_item.save()

            return redirect("/check_out/")
        data = {
        
        
            'cart_count': cart_count,
            'cart_product': cart_product,
            'main_Category':main_Category(request),
                'sub_category':sub_category(request)
        }



        return render(request, 'Cart.html',data)

    except:
     return redirect('/login/?message=Please login')  


######################################  CART METHOD CLOSE ################################################


######################################  REMOVE METHOD START ###############################################

def remove_product(request):
    try:
            user_id = request.session.get('user_uid')
            print(user_id )
            user = Eurekaforbes_User.objects.get(user_uid=user_id)
            print(user )
            if request.method == 'POST':
                remove_product_id = request.POST.get('remove')
            
                remove_id = get_object_or_404(addcart, id=remove_product_id)
                remove_id.delete()
                return redirect('/cart/')
            #return  HttpResponse('remove product')

    except:
     return redirect('/login/?message=Please login')    
    
######################################  REMOVE METHOD CLOSE ##################################################

######################################  CHECK OUT  METHOD START###############################################



def check_out(request):
    try:
        user_id = request.session.get('user_uid')
        cart_product = addcart.objects.filter(user_uid=user_id)
        cart_count = cart_product.count()
        user = Eurekaforbes_User.objects.get(user_uid=user_id)
        cart_products = addcart.objects.filter(user_uid=user_id)


        if request.method == 'POST':
            firstName = request.POST.get('firstName')
            lastName = request.POST.get('lastName')
            mobileNumber = request.POST.get('mobileNumber')
            email = request.POST.get('email')
            houseNo = request.POST.get('houseNo')
            street = request.POST.get('street')
            street1 = request.POST.get('street1')
            street2 = request.POST.get('street2')
            pinCode = request.POST.get('pinCode')
            city = request.POST.get('city')
            country = request.POST.get('country')
            region = request.POST.get('region')

            order_id = str(uuid.uuid4().hex[:10])
            order_date = datetime.now()

            for o in cart_products:
                product_id = o.Product_id
                order = Order(
                    email=user.email,
                    user_uid=user_id,
                    Product_id=o.Product_id,
                    price=o.price,
                    qty=o.qty,
                    total_amount=o.total_amount,
                    first_name=firstName,
                    last_name=lastName,
                    mobile_number=mobileNumber,
                    house_no=houseNo,
                    street=street,
                    street1=street1,
                    street2=street2,
                    pin_code=pinCode,
                    city=city,
                    country=country,
                    region=region,
                    order_id=order_id,
                    order_date=order_date,
                    order_status="New",
                    tracking_id="",
                    tracking_link="",
                    img1=o.img1
                )
                order.save()
                
                last_order = Order.objects.filter(order_id=order_id).last()
                return redirect(f'/Payments/?id={last_order.id}')
                # return HttpResponse('test') 
        data={
            'main_Category':main_Category(request),
                'sub_category':sub_category(request),
                'cart_count': cart_count,
                
            }    

        return render(request, 'Checkout.html',data)
    except:
     return redirect('/login/?message=Please login')   
######################################  CHECK OUT  METHOD CLOSE ###############################################

 
######################################  PAYMENT  METHOD START ##################################################

def Payment(request):
    try:
        user_id = request.session.get('user_uid')
        user = Eurekaforbes_User.objects.get(user_uid=user_id)

        return HttpResponse('payment Page')
    except:
     return redirect('/login/?message=Please login') 


######################################  PAYMENT  METHOD CLOSE ##################################################



from django.shortcuts import render, get_object_or_404

def ProductMain_Category(request, id):
    try:
        user_id = request.session.get('user_uid')
        main_category = get_object_or_404(Main_Category, id=id)
        user = Eurekaforbes_User.objects.get(user_uid=user_id)
    
        all_products = Product.objects.filter(main_category=main_category)
        cart_product = addcart.objects.filter(user_uid=user_id)
        cart_count = cart_product.count()
        
        data = {
        
            'product': all_products,
            'cart_count': cart_count,
            'category_value': all_products,
            'main_Category':main_Category(request),
            'sub_category':sub_category(request)
        }
        return render(request, 'Product.html', data)
    except:
     return redirect('/login/?message=Please login')     



    



def Productsub_Category(request, id):
    try:
        user_id = request.session.get('user_uid')
        user = Eurekaforbes_User.objects.get(user_uid=user_id)

   
        
        try:
            sub_category_instance = get_object_or_404(Sub_Category, id=id)
            print(f'main_category= {sub_category_instance.main_category} ,sub_category = {sub_category_instance.Sub_Categorytype}')
            
            all_products = Product.objects.filter(main_category=sub_category_instance.main_category, sub_category=sub_category_instance)
            
        except Sub_Category.DoesNotExist:
            all_products = None    
            print('No data for the given Sub_Category id')
        
        cart_product = addcart.objects.filter(user_uid=user_id)
        cart_count = cart_product.count()
        
        data = {
            'product': all_products,
            'cart_count': cart_count,
            'category_value': all_products,
            'sub_category_instance': sub_category_instance,
            'main_Category': main_Category(request),
            'sub_category': sub_category(request) 
        }
        
        return render(request, 'Product.html', data)
    except:
     return redirect('/login/?message=Please login')     


######################################   CATEGORY  METHOD CLOSE ##################################################


######################################   COUNTING  METHOD START ###################################################

def cart_count(request):
    try:

        user_id = request.session.get('user_uid')
        user = Eurekaforbes_User.objects.get(user_uid=user_id)
        print('user',user)
        cart_product = addcart.objects.filter(user_uid=user_id)
        cart_count = cart_product.count()
        print(cart_count )
        return render(request, 'header.html', {'cart_count': cart_count})

    except:
     return redirect('/login/?message=Please login')     








######################################   COUNTING  METHOD CLOSE ###################################################

###################################### HEADER METHOD  START #######################################################
def header(request):
        try:
            user_id = request.session.get('user_uid')
            user = Eurekaforbes_User.objects.get(user_uid=user_id)
            print('user',user)
            user_id = request.session.get('user_uid')
            user = Eurekaforbes_User.objects.get(user_uid=user_id)
        
            cart_product = addcart.objects.filter(user_uid=user_id)
            cart_count = cart_product.count()
            data={
                
                'cart_count': cart_count,
                'main_Category':main_Category(request),
                    'sub_category':sub_category(request)
            }

            return render(request,'header.html',data)

    
        except:
            return redirect('/login/?message=Please login')     




###################################### HEADER METHOD  CLOSE #######################################################
def Slider(request):
    try:
            user_id = request.session.get('user_uid')
            user = Eurekaforbes_User.objects.get(user_uid=user_id)
            print('user',user)
            return render(request, 'Slider.html')
    except:
        return redirect('/login/?message=Please login') 


def footer(request):
    try:
            user_id = request.session.get('user_uid')
            user = Eurekaforbes_User.objects.get(user_uid=user_id)
            print('user',user)
            return render(request,'footer.html')
    except:
        return redirect('/login/?message=Please login') 




################################################################################### ################################################

'''


def Productsub_Category(request, id):
    user_id = request.session.get('user_uid')
    # main_category = get_object_or_404(Main_Category, id=id)
    # print('main_category', main_category)
    
    try:

        sb = Sub_Category.objects.get(id=id)
        print(f'main_category= {sb.main_category} ,sub_category = {sb.Sub_Categorytype}')
        all_products = Product.objects.filter(main_category = sb.main_category ,sub_category = sb.Sub_Category)
        
    except:
        all_products = None    
        print('no dATA')
    
    cart_product = addcart.objects.filter(user_uid=user_id)
    cart_count = cart_product.count()
    
    data = {
       
        'product': all_products,
        'cart_count': cart_count,
        'category_value': all_products,
        'main_Category':main_Category(request),
        'sub_category':sub_category(request)
    }
    return render(request, 'Product.html', data)

'''






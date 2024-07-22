from django.shortcuts import render
from django.http import HttpResponse
from Orders.models import Order
from Cart.models import addcart
from Admin.models import admin_user
from Product.models import *


from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ProductForm, MainCategoryForm, SubCategoryForm
from .models import admin_user


from django.shortcuts import render, redirect
'''
def admin_login(request):
       
    # if request.session.get('customer_user_id'):
    #     return redirect('/admin/dashboard/')
   
    if request.method == 'POST':
        email = request.POST.get('email')
        print('email',email)
        password = request.POST.get('password')
        remember_me = request.POST.get('remember_me')  # Retrieve the remember_me field
       
        
        try:
            # Authenticate user
            user = admin_user.objects.get(customer_email=email)
            
            # Check user's password
            if user.customer_password == password:
                
                if remember_me == 'on':
                    request.session.set_expiry(2592000)  
                else:
                    
                    request.session.set_expiry(0)
                
                # Store reseller_id in session
                request.session['customer_id'] = str(user.customer_id)
                # return HttpResponse('test')
             
                return redirect('/Admin/panel/dashboard/')
            else:
                return render(request, 'admin login.html', {'error': 'Invalid password'})
        
        except admin_user.DoesNotExist:
            # User with given email does not exist
            return render(request, 'admin login.html', {'error': 'Invalid email'})
    return render (request,'admin login.html')
'''
from django.views.decorators.csrf import csrf_protect

########################################### LOGIN METHOD  START ############################################# 

@csrf_protect
def admin_login(request):
    if request.session.get('customer_id'):
        return redirect('/admin/panel/dashboard/')
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        remember_me = request.POST.get('remember_me')  
       
        try:
    
            user = admin_user.objects.get(customer_email=email)
            print(f'User found: {user.customer_email}')
            
 
            if user.customer_password == password:
                print('Password matched')

                if remember_me == 'on':
                    request.session.set_expiry(2592000)  
                else:
                    request.session.set_expiry(0)  
                
              
                request.session['customer_id'] = str(user.customer_id)
             
                return redirect('/admin/panel/dashboard/')
            else:
                print('Invalid password')
                return render(request, 'admin_login.html', {'error': 'Invalid password'})
        
        except admin_user.DoesNotExist:
   
            print('User does not exist')
            return render(request, 'admin_login.html', {'error': 'Invalid email'})

    return render(request, 'admin_login.html')

########################################### LOGIN METHOD  CLODE ############################################# 

###########################################  DASHBOARD START ################################################
from django.views.decorators.csrf import csrf_protect
@csrf_protect
def Dashboard(request):
    try:
        admin_id = request.session.get('customer_id')
        if not admin_id:
            return redirect('/admin/panel/?message=Please login')

        admin = admin_user.objects.get(customer_id=admin_id)

        # Fetch order counts for each status
        all_orders_count = Order.objects.all().count()
        new_orders_count = Order.objects.filter(order_status='New').count()
        shipped_orders_count = Order.objects.filter(order_status='shipped').count()
        delivered_orders_count = Order.objects.filter(order_status='delivered').count()
        ready_orders_count = Order.objects.filter(order_status='ready').count()
        canceled_orders_count = Order.objects.filter(order_status='canceled').count()

        context = {
            'all_orders_count': all_orders_count,
            'new_orders_count': new_orders_count,
            'shipped_orders_count': shipped_orders_count,
            'delivered_orders_count': delivered_orders_count,
            'ready_orders_count': ready_orders_count,
            'canceled_orders_count': canceled_orders_count,
        }

        return render(request, 'dashboard.html', context)

    except admin_user.DoesNotExist:
        return redirect('/admin/panel/?message=Please login')



###########################################  DASHBOARD CLOSE ############################################# 
def orders(request):
    try:
        admin_id = request.session.get('customer_id')
        admin = admin_user.objects.get(customer_id=admin_id)
            
        # all_orders = Order.objects.all() 
        
        # Fetch order counts for each status
        all_orders_count = Order.objects.all().count()
        new_orders_count = Order.objects.filter(order_status='New').count()
        shipped_orders_count = Order.objects.filter(order_status='shipped').count()
        delivered_orders_count = Order.objects.filter(order_status='delivered').count()
        ready_orders_count = Order.objects.filter(order_status='ready').count()
        canceled_orders_count = Order.objects.filter(order_status='canceled').count()

        data={
            'orders': all_orders,
            'all_orders_count': all_orders_count,
            'new_orders_count': new_orders_count,
            'shipped_orders_count': shipped_orders_count,
            'delivered_orders_count': delivered_orders_count,
            'ready_orders_count': ready_orders_count,
            'canceled_orders_count': canceled_orders_count,
        }
        return render (request,'admin orders.html', data)
    except admin_user.DoesNotExist:
        return redirect('/admin/panel/?message=Please login')







def all_orders(request):
    orders = Order.objects.all()
    all_orders_count = orders.count()
    return render(request, 'admin order_detail.html', {'orders': orders, 'all_orders_count': all_orders_count})

def new_orders(request):
    orders = Order.objects.filter(order_status='New')
    order_count = orders.count()
    return render(request, 'admin order_detail.html', {'orders': orders, 'order_count': order_count})

def shipped_orders(request):
    orders = Order.objects.filter(order_status='shipped')
    order_count = orders.count()
    return render(request, 'admin order_detail.html', {'orders': orders, 'order_count': order_count})

def deliver_orders(request):
    orders = Order.objects.filter(order_status='delivered')
    order_count = orders.count()
    return render(request, 'admin order_detail.html', {'orders': orders, 'order_count': order_count})



def ready_orders(request):
    orders = Order.objects.filter(order_status='ready')
    ready_orders_count = orders.count()
    print('ready_orders_countttttttttttttttt',ready_orders_count)
    return render(request, 'admin order_detail.html', {'orders': orders, 'ready_orders_count': ready_orders_count})



def cancel_orders(request):
    orders = Order.objects.filter(order_status='canceled')
    order_count = orders.count()
    return render(request, 'admin order_detail.html', {'orders': orders, 'order_count': order_count})



def accept_order(request):

        admin_id = request.session.get('customer_id')
        admin = admin_user.objects.get(customer_id=admin_id)
        
        order_id = request.GET.get('id')  # Use get() method to safely retrieve query parameter
        order = Order.objects.get(order_id=order_id)
        
        # Assuming you want to change the order status to "ready"
        order.order_status = "ready"
        order.save()

        # return HttpResponse('Order status updated successfully') 
        
        return redirect('/admin/panel/Ready_orders/')

  

def admin_ship_order(request):
   
        admin_id = request.session.get('customer_id')
        admin = admin_user.objects.get(customer_id=admin_id)
        #  Order_i = request.GET['oid']
        if request.method == 'GET':
            Order_i = request.GET.get('idd')
            tracking_link = request.GET.get('link')
            tracking_id = request.GET.get('tracking_id')

            
            order= Order.objects.get(order_id = Order_i)
            order.order_status = 'shipped'
            order.tracking_link = tracking_link
            order.tracking_id = tracking_id
            order.save()
            return HttpResponse('Order status updated successfully') 
            # return redirect('/admin/panel/Reseller_shipped_orders/')

def admin_deliver_order(request):
  
        
        admin_id = request.session.get('customer_id')
        admin = admin_user.objects.get(customer_id=admin_id)
       
        if request.method == 'GET':
            Order_i = request.GET.get('deliver')
            print(f"Order ID to deliver: {Order_i}")

            order= Order.objects.get(order_id = Order_i)
            # order = get_object_or_404(Order, order_id=Order_i)
            order.order_status = 'delivered'
            order.save()
            return HttpResponse('test')
            
            # return redirect('/admin/panel/Reseller_delivered_orders/')


def admin_cancel_order(request):
  
        
        admin_id = request.session.get('customer_id')
        admin = admin_user.objects.get(customer_id=admin_id)
       
        if request.method == 'GET':
            Order_i = request.GET.get('cancel')
            print(f"Order ID to deliver: {Order_i}")

            order= Order.objects.get(order_id = Order_i)
            # order = get_object_or_404(Order, order_id=Order_i)
            order.order_status = 'canceled'
            order.save()
            return HttpResponse('test')
            
            # return redirect('/admin/panel/admin_Cancel_order/')



###########################################  ADD PRODUCT START #############################################   

def Add_product_detail(request):
    try:
        admin_id = request.session.get('customer_id')
        admin = admin_user.objects.get(customer_id=admin_id)
        
        if request.method == 'POST':
            product_form = ProductForm(request.POST, request.FILES)
            if product_form.is_valid():
                product_form.save()
                # return HttpResponse('test')
                return redirect('/admin/panel/dashboard/')
        else:
            product_form = ProductForm()
            
        return render(request, 'admin Productform.html', {'product_form': product_form})
    except admin_user.DoesNotExist:
        return redirect('/admin/panel/?message=Please login')
###########################################  EDIT PRODUCT CLOSE #############################################   

###########################################  BANNER METHOD START #############################################   


from django.shortcuts import render, redirect
from Galleryapp.models import Page
from .forms import PageForm

def edit_banner(request):
    try:
        page = Page.objects.first()  # Assuming there is only one Page object
        if request.method == 'POST':
            form = PageForm(request.POST, request.FILES, instance=page)
            if form.is_valid():
                form.save()
                return redirect('/admin/panel/dashboard/')
        else:
            form = PageForm(instance=page)
        
        context = {
            'form': form,
            'page': page,
        }
        return render(request, 'Admin edit_banner.html', context)
    except Page.DoesNotExist:
        # Handle the case where Page object does not exist (not likely in this context)
        return redirect('/')  # Redirect to homepage or handle appropriately
    


###########################################  BANNER METHOD CLOSE #############################################  
            
###########################################  EDIT PRODUCT START #############################################   
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def edit_product(request):
    try:
        if request.method == 'POST':
            admin_id = request.session.get('customer_id')
            admin = admin_user.objects.get(customer_id=admin_id)
            product_i = request.GET.get('idd')
            product = Product.objects.get(Product_id=product_i)

            product.active_product = request.POST.get('active_product') == 'true'  # Convert string to boolean
            product.order_status =request.POST.get('order_status')
            product.name = request.POST.get('name')
            product.price = request.POST.get('price')
            product.sku_code = request.POST.get('sku_code')
            product.mrp = request.POST.get('mrp')
            product.sub_title = request.POST.get('sub_title')
            product.brand = request.POST.get('brand')
            product.color = request.POST.get('color')
            
            # Pehle category ID retrieve karo form se
            main_category_id = request.POST['main_category']
            # Fir usse related Main_Category instance retrieve karo
            main_category = Main_Category.objects.get(id=main_category_id)
            # Ab product.main_category ko correct instance assign karo
            product.main_category = main_category

            # Similarly, handle sub_category
            sub_category_id = request.POST['sub_category']
            sub_category = Sub_Category.objects.get(id=sub_category_id)
            product.sub_category = sub_category

            # Baaki fields
            product.model_name = request.POST.get('model_name')
            product.warranty = request.POST.get('warranty')
            product.technology = request.POST.get('technology')
            product.feature = request.POST.get('feature')
            product.product_type = request.POST.get('product_type')
            product.description = request.POST.get('description')
            product.stock = request.POST.get('stock')
            product.qty1 = request.POST.get('qty1')
            product.qty2 = request.POST.get('qty2')
            product.qty3 = request.POST.get('qty3')
            product.qty4 = request.POST.get('qty4')
            product.qty5 = request.POST.get('qty5')
            product.qty6 = request.POST.get('qty6')
            product.qty7 = request.POST.get('qty7')
            product.qty8 = request.POST.get('qty8')
            product.qty9 = request.POST.get('qty9')
            product.qty10 = request.POST.get('qty10')
            product.weight = request.POST.get('weight')
            product.dimensions = request.POST.get('dimensions')
            product.installation_type = request.POST.get('installation_type')
            product.storage_capacity = request.POST.get('storage_capacity')
            product.purification_modules = request.POST.get('purification_modules')
            product.input_water_pressure = request.POST.get('input_water_pressure')
            product.input_water_temperature = request.POST.get('input_water_temperature')
            product.input_water_chlorine_max = request.POST.get('input_water_chlorine_max')
            product.input_water_tds = request.POST.get('input_water_tds')
            product.uv_lamp = request.POST.get('uv_lamp')
            product.uv_lamp_life = request.POST.get('uv_lamp_life')
            product.power_consumption = request.POST.get('power_consumption')
            product.operating_input_voltage = request.POST.get('operating_input_voltage')
            product.included_in_box = request.POST.get('included_in_box')
            product.product_warranty = request.POST.get('product_warranty')

            product.save()
            return redirect('/admin/panel/dashboard/')
            # return HttpResponse('Product updated successfully')

        else:
            # Fetch data for rendering the form initially
            admin_id = request.session.get('customer_id')
            admin = admin_user.objects.get(customer_id=admin_id)
            product_i = request.GET.get('idd')
            product = Product.objects.get(Product_id=product_i)
            main_categories = Main_Category.objects.all()
            sub_categories = Sub_Category.objects.all()

        data = {
            'product': product,
            'main_categories': main_categories,
            'sub_categories': sub_categories,
        }
        return render(request, 'admin EditProduct .html', data)
    except admin_user.DoesNotExist:
        return redirect('/admin/panel/?message=Please login')
    
###########################################  EDIT PRODUCT  CLOSE  #############################################  
 
#############################################   INVENTORY   START ################################################ 

def inventory(request):
    try:
        admin_id = request.session.get('customer_id')
        
        cart_product = addcart.objects.filter(user_uid=admin_id) 
        cart_count = cart_product.count()

        active_order_count = Product.objects.filter(active_product=True).count()
        inactive_order_count = Product.objects.filter(active_product=False).count()
        outofstock_order_count = Product.objects.filter(stock=1).count()
        Instock_order_count = Product.objects.filter(stock=0).count()
        
        data = {
            'Instock_order_count': Instock_order_count,
            'outofstock_order_count': outofstock_order_count,
            'cart_count': cart_count,
            'active_order_count': active_order_count,
            'inactive_order_count': inactive_order_count,
        }
    
        return render(request, 'admin Inventory.html', data)
    except admin_user.DoesNotExist:
        return redirect('/admin/panel/?message=Please login')

def active_product(request):
    try:
        admin_id = request.session.get('customer_id')
        
        admin = admin_user.objects.get(customer_id=admin_id) 

        active_products = Product.objects.filter(active_product=True)
        cart_product = addcart.objects.filter(user_uid=admin_id) 
        cart_count = cart_product.count()

        data = {
            'products': active_products, 
            'cart_count': cart_count,
        }

        return render(request, "admin Inventory detail.html", data)
    except admin_user.DoesNotExist:
        return redirect('/admin/panel/?message=Please login')

def inactive_product(request):
    try:
        admin_id = request.session.get('customer_id')
        
        admin = admin_user.objects.get(customer_id=admin_id)

        inactive_products = Product.objects.filter(active_product=False)
        cart_product = addcart.objects.filter(user_uid=admin_id) 
        cart_count = cart_product.count()

        data = {
            'products': inactive_products,  # Pass queryset of active products
            'cart_count': cart_count,
        }

        return render(request, "admin Inventory detail.html", data)
    except admin_user.DoesNotExist:
        return redirect('/admin/panel/?message=Please login')



def Outof_Stock(request):
    try:
        admin_id = request.session.get('customer_id')
    
        admin = admin_user.objects.get(customer_id=admin_id)
        cart_product = addcart.objects.filter(user_uid=admin_id) 
        cart_count = cart_product.count()

        print('cart_counttttt', cart_count)

        products = Product.objects.filter(stock=1)
        reseller_outofstock_order_count = products.count()
       

        context = {
            'products': products,
            'cart_count': cart_count,
        }
        return render(request, 'admin Stockpage.html', context)
    except admin_user.DoesNotExist:
        return redirect('/admin/panel/?message=Please login')



def In_Stock(request):
    try:
            admin_id = request.session.get('customer_id')
    
            admin = admin_user.objects.get(customer_id=admin_id)
            cart_product = addcart.objects.filter(user_uid=admin_id) 
            cart_count = cart_product.count()

            print('cart_counttttt', cart_count)

            products = Product.objects.filter(  stock = 0)
            reseller_outofstock_order_count = products.count()
           

            context = {
                'products': products,
                'cart_count': cart_count,
            }
            return render(request, 'admin Stockpage.html', context)
    

    except admin_user.DoesNotExist:
        return redirect('/admin/panel/?message=Please login')




###########################################  PAYMENT START #############################################   

# def payment(request):
#     try:
#         admin_id = request.session.get('customer_id')
#         admin = admin_user.objects.get(customer_id=admin_id)
#         all_payments = Order.objects.all()  
#         return render(request, 'payment.html', {'payments': all_payments})
#     except admin_user.DoesNotExist:
#         return redirect('/admin/panel/login/?message=Please login')


# from django.shortcuts import render, get_object_or_404
###########################################  PAYMENT  ###############################################  

############################ HEADER ##################################################################


def admin_header(request):

    
        return render(request,"admin header.html") 



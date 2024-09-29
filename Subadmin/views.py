from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect

from Subadmin.models import Subadmin
from django.views.decorators.csrf import csrf_protect

from Orders.models import Order
from Cart.models import addcart
from Admin.models import admin_user

from django.shortcuts import render, redirect
from .models import  Subadmin

from Product.models import Product


########################################### LOGIN METHOD  START ############################################# 

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def Subadmin_login(request):
    if request.session.get('Sub_admin_id'):
        return redirect('/subadmin/panel/subadmin_dashboard/')
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        remember_me = request.POST.get('remember_me')  
       
        try:
    
            user = Subadmin.objects.get(Sub_admin_email=email)
            print(f'User found: {user.Sub_admin_email}')
            
 
            if user.Sub_admin_password == password:
                print('Password matched')

                if remember_me == 'on':
                    request.session.set_expiry(2592000)  
                else:
                    request.session.set_expiry(0)  
                
              
                request.session['Sub_admin_id'] = str(user.Sub_admin_id)
             
                return redirect('/subadmin/panel/subadmin_dashboard/')
            else:
                print('Invalid password')
                return render(request, 'Subadmin_login.html', {'error': 'Invalid password'})
        
        except Subadmin.DoesNotExist:
   
            print('User does not exist')
            return render(request, 'Subadmin_login.html', {'error': 'Invalid email'})

    return render(request, 'Subadmin_login.html')



def Sub_Dashboard(request):
  #  try:
        subadmin_id = request.session.get('Sub_admin_id')
        admin = Subadmin.objects.get(Sub_admin_id=subadmin_id)

    
        data = {
                'orders_count':suball_count(request),

        }
        return render(request,'Subadmin_dashboard.html',data)
    
    # except Subadmin.DoesNotExist:
    #     return redirect('/subadmin/panel/')  
 
    # except:
    #     return redirect('/subadmin/panel/') 


######################################################################################################
def Subadmin_orders(request):
    try:
        subadmin_id = request.session.get('Sub_admin_id')
        admin = Subadmin.objects.get(Sub_admin_id=subadmin_id)


        all_ord = Order.objects.filter(Sub_admin=subadmin_id)
        print('all_orddddddddddddddddddddddddddddddd',all_ord)

        data = {
            'suborders': all_ord,
                'orders_count':suball_count(request),
                'new_orders_count':subnew_count(request),
                'ship_orders_count':subship_count(request),
                'ready_orders_count':subready_count(request),
                'deliver_orders_count':subdeliver_count(request),
                'cancel_orders_count':subcancel_count(request),
                'failed_orders_count':Order.objects.filter(Sub_admin=subadmin_id, order_status='Failed').count()
                

        }
    
        return render (request,'Subadmin_Order.html',data)
    except Subadmin.DoesNotExist:
        return redirect('/subadmin/panel/')  
 
    except:
        return redirect('/subadmin/panel/') 



          
###########################################  EDIT PRODUCT START #############################################   

@csrf_exempt
def subadmin_addproduct(request):
    try:
            subadmin_id = request.session.get('Sub_admin_id')
            admin = Subadmin.objects.get(Sub_admin_id=subadmin_id)


            if request.method == 'POST':
                # Extract data from POST request
                name = request.POST.get('name')
                title = request.POST.get('title')
                sub_title = request.POST.get('sub_title')
                price = request.POST.get('price')
                mrp = request.POST.get('mrp')
                sku_code = request.POST.get('sku_code')
                brand = request.POST.get('brand')
                color = request.POST.get('color')
            

                    # Pehle category ID retrieve karo form se
                main_category_id = request.POST['main_category']
                # Fir usse related Main_Category instance retrieve karo
                main_category = Main_Category.objects.get(id=main_category_id)
                # Ab product.main_category ko correct instance assign karo
                main_category = main_category

                # Similarly, handle sub_category
                sub_category_id = request.POST['sub_category']
                sub_category = Sub_Category.objects.get(id=sub_category_id)
                sub_category = sub_category

                model_name = request.POST.get('model_name')
                warranty = request.POST.get('warranty')
                technology = request.POST.get('technology')
                feature = request.POST.get('feature')
                product_type = request.POST.get('product_type')
                description = request.POST.get('description')
                active_product = request.POST.get('active_product') == 'true'
                order_status = request.POST.get('order_status')
                stock = request.POST.get('stock')
                qty1 = request.POST.get('qty1')
                qty2 = request.POST.get('qty2')
                qty3 = request.POST.get('qty3')
                qty4 = request.POST.get('qty4')
                qty5 = request.POST.get('qty5')
                qty6 = request.POST.get('qty6')
                qty7 = request.POST.get('qty7')
                qty8 = request.POST.get('qty8')
                qty9 = request.POST.get('qty9')
                qty10 = request.POST.get('qty10')
                weight = request.POST.get('weight')
                dimensions = request.POST.get('dimensions')
                installation_type = request.POST.get('installation_type')
                storage_capacity = request.POST.get('storage_capacity')
                purification_modules = request.POST.get('purification_modules')
                input_water_pressure = request.POST.get('input_water_pressure')
                input_water_temperature = request.POST.get('input_water_temperature')
                input_water_chlorine_max = request.POST.get('input_water_chlorine_max')
                input_water_tds = request.POST.get('input_water_tds')
                uv_lamp = request.POST.get('uv_lamp')
                uv_lamp_life = request.POST.get('uv_lamp_life')
                power_consumption = request.POST.get('power_consumption')
                operating_input_voltage = request.POST.get('operating_input_voltage')
                included_in_box = request.POST.get('included_in_box')
                product_warranty = request.POST.get('product_warranty')
                # sub_admin = Sub_admin_id
                Sub_admin = subadmin_id

                # Handle file uploads
                img1 = request.FILES.get('img1')
                img2 = request.FILES.get('img2')
                img3 = request.FILES.get('img3')
                img4 = request.FILES.get('img4')
                img5 = request.FILES.get('img5')
                img6 = request.FILES.get('img6')
                img7 = request.FILES.get('img7')
                img8 = request.FILES.get('img8')

                # Create and save the Product
                product = Product(
                    name=name,
                    title=title,
                    sub_title=sub_title,
                    price=price,
                    mrp=mrp,
                    sku_code=sku_code,
                    brand=brand,
                    color=color,
                    main_category_id=main_category_id,
                    sub_category_id=sub_category_id,
                    model_name=model_name,
                    warranty=warranty,
                    technology=technology,
                    feature=feature,
                    product_type=product_type,
                    description=description,
                    active_product=active_product,
                    order_status=order_status,
                    stock=stock,
                    qty1=qty1,
                    qty2=qty2,
                    qty3=qty3,
                    qty4=qty4,
                    qty5=qty5,
                    qty6=qty6,
                    qty7=qty7,
                    qty8=qty8,
                    qty9=qty9,
                    qty10=qty10,
                    weight=weight,
                    dimensions=dimensions,
                    installation_type=installation_type,
                    storage_capacity=storage_capacity,
                    purification_modules=purification_modules,
                    input_water_pressure=input_water_pressure,
                    input_water_temperature=input_water_temperature,
                    input_water_chlorine_max=input_water_chlorine_max,
                    input_water_tds=input_water_tds,
                    uv_lamp=uv_lamp,
                    uv_lamp_life=uv_lamp_life,
                    power_consumption=power_consumption,
                    operating_input_voltage=operating_input_voltage,
                    included_in_box=included_in_box,
                    product_warranty=product_warranty,
                    Sub_admin=Sub_admin,
                    img1=img1,
                    img2=img2,
                    img3=img3,
                    img4=img4,
                    img5=img5,
                    img6=img6,
                    img7=img7,
                    img8=img8,
                )
                product.save()
                return redirect('/subadmin/panel/subadmin_dashboard/')
            else:
                subadmin_id = request.session.get('Sub_admin_id')
                admin = Subadmin.objects.get(Sub_admin_id=subadmin_id)
            
                main_categories = Main_Category.objects.all()
                sub_categories = Sub_Category.objects.all()
                data={
                # 'product': product,
                'main_categories': main_categories,
                'sub_categories': sub_categories,
                }

                # Redirect to a success page or product list
            

            return render(request, 'subadmin_add_product.html',data)

    except Subadmin.DoesNotExist:
        return redirect('/subadmin/panel/')  
 
    except:
        return redirect('/subadmin/panel/') 


###################################################################################################
@csrf_exempt
def subadmin_edit_product(request):

    try:
        subadmin_id = request.session.get('Sub_admin_id')
        admin = Subadmin.objects.get(Sub_admin_id=subadmin_id)
        if request.method == 'POST':
         
            product_i = request.GET.get('iddd')
            product = Product.objects.get(Product_id=product_i)

            product.active_product = request.POST.get('active_product') == 'on'  # Convert string to boolean
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
            product.Sub_admin = subadmin_id
            

            product.save()
            return redirect('/subadmin/panel/subadmin_Inventory/')
        #     # return HttpResponse('Product updated successfully')

        else:
            # Fetch data for rendering the form initially
            subadmin_id = request.session.get('Sub_admin_id')
            admin = Subadmin.objects.get(Sub_admin_id=subadmin_id)
            product_i = request.GET.get('iddd')
            product = Product.objects.get(Product_id=product_i)
            main_categories = Main_Category.objects.all()
            sub_categories = Sub_Category.objects.all()

        data = {
            'product': product,
            'main_categories': main_categories,
            'sub_categories': sub_categories,
        }
        return render(request, 'subadmin_Edit_product.html',data)
    except Subadmin.DoesNotExist:
        return redirect('/subadmin/panel/')  
 
    except:
        return redirect('/subadmin/panel/') 
   



from Product.models import Product, Main_Category, Sub_Category
from django.shortcuts import render, redirect


def subadmin_add_main_category(request):
    try:
        subadmin_id = request.session.get('Sub_admin_id')
        admin = Subadmin.objects.get(Sub_admin_id=subadmin_id)
        if request.method == 'POST':
            # Retrieve form data
            main_category_name = request.POST.get('main_Category')
            main_category_type = request.POST.get('main_Categorytype')
            
            if main_category_name and main_category_type:
                # Create a new Main_Category instance
                main_category = Main_Category(
                    main_Category=main_category_name,
                    main_Categorytype=main_category_type
                )
                
                # Save the instance to the database
                main_category.save()
                
                # Redirect to a success page or another view
                return redirect('/subadmin/panel/subadmin_dashboard/')
    
        return render(request, 'subadmin add_main_category.html')
    
    except Subadmin.DoesNotExist:
        return redirect('/subadmin/panel/')  
 
    except:
        return redirect('/subadmin/panel/') 
 


def subadmin_add_sub_category(request):
    try:
        subadmin_id = request.session.get('Sub_admin_id')
        admin = Subadmin.objects.get(Sub_admin_id=subadmin_id)
        sub_category_name = request.POST.get('sub_Category')
        sub_category_type = request.POST.get('Sub_Categorytype')
            
        if sub_category_name and sub_category_type:
                # Create and save a new Sub_Category instance
                new_sub_category = Sub_Category(
                    Sub_Category=sub_category_name,
                    Sub_Categorytype=sub_category_type
                )
                new_sub_category.save()
                
                # Redirect to a success page or another view
                return redirect('/subadmin/panel/subadmin_dashboard/')
                    # Fetch all main categories to populate the select field
        main_categories = Main_Category.objects.all()
        data = {
            'main_categories': main_categories
        }
        
    
        return render(request, 'subadmin add_sub_category.html',data)
    
    except Subadmin.DoesNotExist:
        return redirect('/subadmin/panel/')  
 
    except:
        return redirect('/subadmin/panel/') 
  
###################################################################################################
def subadmin_inventory(request):
    try:
        subadmin_id = request.session.get('Sub_admin_id')
        admin = Subadmin.objects.get(Sub_admin_id=subadmin_id)


        
        active_order_count = Product.objects.filter(active_product=True,Sub_admin=subadmin_id).count()
        inactive_order_count = Product.objects.filter(active_product=False,Sub_admin=subadmin_id).count()
        outofstock_order_count = Product.objects.filter(stock=1,Sub_admin=subadmin_id).count()
        Instock_order_count = Product.objects.filter(stock=0,Sub_admin=subadmin_id).count()
        
        data = {
                'Instock_order_count': Instock_order_count,
                'outofstock_order_count': outofstock_order_count,
            
                'active_order_count': active_order_count,
                'inactive_order_count': inactive_order_count,
        }
        
        return render(request, 'subadmin_inventory.html',data)
    
    except Subadmin.DoesNotExist:
        return redirect('/subadmin/panel/')  
 
    except:
        return redirect('/subadmin/panel/') 



def subadmin_active_product(request):
    try:
        subadmin_id = request.session.get('Sub_admin_id')
        admin = Subadmin.objects.get(Sub_admin_id=subadmin_id)

        active_products = Product.objects.filter(active_product=True,Sub_admin=subadmin_id)
        cart_product = addcart.objects.filter(user_uid=subadmin_id) 
        data={
                'products': active_products, 
        } 

        return render(request, 'subadmin_inventory_detail.html',data)
    except Subadmin.DoesNotExist:
        return redirect('/subadmin/panel/')  
 
    except:
        return redirect('/subadmin/panel/') 

def subadmin_inactive_product(request):
    try:
        subadmin_id = request.session.get('Sub_admin_id')
        admin = Subadmin.objects.get(Sub_admin_id=subadmin_id)

        inactive_products = Product.objects.filter(active_product=False,Sub_admin=subadmin_id)
        cart_product = addcart.objects.filter(user_uid=subadmin_id) 
        data={
            'products': inactive_products,
        }
        return render(request, 'subadmin_inventory_detail.html',data)
    except Subadmin.DoesNotExist:
        return redirect('/subadmin/panel/')  
 
    except:
        return redirect('/subadmin/panel/') 


def subadmin_Outof_Stock(request):
    try:
        subadmin_id = request.session.get('Sub_admin_id')
        admin = Subadmin.objects.get(Sub_admin_id=subadmin_id)

        cart_product = addcart.objects.filter(user_uid=subadmin_id) 
        cart_count = cart_product.count()



        products = Product.objects.filter(stock=1,Sub_admin=subadmin_id)
        subadmin_outofstock_order_count = products.count()
        data={
            'products': products,
        }
    
        return render(request, 'subadmin_Stockpage.html',data)
    except Subadmin.DoesNotExist:
        return redirect('/subadmin/panel/')  
 
    except:
        return redirect('/subadmin/panel/') 

def subadmin_In_Stock(request):
    try:
        subadmin_id = request.session.get('Sub_admin_id')
        admin = Subadmin.objects.get(Sub_admin_id=subadmin_id)
        cart_product = addcart.objects.filter(user_uid=subadmin_id) 
        cart_count = cart_product.count()

    

        products = Product.objects.filter(  stock = 0,Sub_admin=subadmin_id)
        subadmin_outofstock_order_count = products.count()
        data={
            'products': products,
        }
        return render(request, 'subadmin_Stockpage.html',data)
    except Subadmin.DoesNotExist:
        return redirect('/subadmin/panel/')  
 
    except:
        return redirect('/subadmin/panel/') 

    
###############################################################################################################

def suball_count(request):
    try:
        subadmin_id = request.session.get('Sub_admin_id')
        admin = Subadmin.objects.get(Sub_admin_id=subadmin_id)
     
        orders_count = Order.objects.filter(Sub_admin=subadmin_id).count()
        return orders_count
    except Subadmin.DoesNotExist:
        return redirect('/subadmin/panel/')  
 
    except:
        return redirect('/subadmin/panel/') 
##################################################################################################################

def subnew_count(request):
    try:
        subadmin_id = request.session.get('Sub_admin_id')
        admin = Subadmin.objects.get(Sub_admin_id=subadmin_id)

        new_orders_count = Order.objects.filter(Sub_admin=subadmin_id, order_status='New').count()
        
        return new_orders_count

    except Subadmin.DoesNotExist:
        return redirect('/subadmin/panel/')  
 
    except:
        return redirect('/subadmin/panel/') 
##################################################################################################################

def subready_count(request):
    try:
        subadmin_id = request.session.get('Sub_admin_id')
        admin = Subadmin.objects.get(Sub_admin_id=subadmin_id)

        ready_orders_count = Order.objects.filter(Sub_admin=subadmin_id, order_status='ready').count()
        
        return ready_orders_count
    except Subadmin.DoesNotExist:
        return redirect('/subadmin/panel/')  
 
    except:
        return redirect('/subadmin/panel/') 

##################################################################################################################

def subship_count(request):
    try:
        subadmin_id = request.session.get('Sub_admin_id')
        admin = Subadmin.objects.get(Sub_admin_id=subadmin_id)

        ship_orders_count = Order.objects.filter(Sub_admin=subadmin_id, order_status='shipped').count()
        
        return ship_orders_count
    except Subadmin.DoesNotExist:
        return redirect('/subadmin/panel/')  
 
    except:
        return redirect('/subadmin/panel/') 

##################################################################################################################

def subdeliver_count(request):
    try:
        subadmin_id = request.session.get('Sub_admin_id')
        admin = Subadmin.objects.get(Sub_admin_id=subadmin_id)

        deliver_orders_count = Order.objects.filter(Sub_admin=subadmin_id, order_status='delivered').count()
        
        return deliver_orders_count
    except Subadmin.DoesNotExist:
        return redirect('/subadmin/panel/')  
 
    except:
        return redirect('/subadmin/panel/') 



##################################################################################################################

def subcancel_count(request):
    try:
        subadmin_id = request.session.get('Sub_admin_id')
        admin = Subadmin.objects.get(Sub_admin_id=subadmin_id)

        cancel_orders_count = Order.objects.filter(Sub_admin=subadmin_id, order_status='canceled').count()
        
        return cancel_orders_count
    except Subadmin.DoesNotExist:
        return redirect('/subadmin/panel/')  
 
    except:
        return redirect('/subadmin/panel/') 

##################################################################################################################


def all_order (request):
    try:
        subadmin_id = request.session.get('Sub_admin_id')
        admin = Subadmin.objects.get(Sub_admin_id=subadmin_id)

        all_ord = Order.objects.filter(Sub_admin=subadmin_id)

        data = {
            'suborders': all_ord,

            'orders_count':suball_count(request),
                'new_orders_count':subnew_count(request),
                'ship_orders_count':subship_count(request),
                'ready_orders_count':subready_count(request),
                'deliver_orders_count':subdeliver_count(request),
                'cancel_orders_count':subcancel_count(request),
                'failed_orders_count':Order.objects.filter(Sub_admin=subadmin_id, order_status='Failed').count()
        
        }
        return render (request,'Subadmin_Orderdetail.html',data)

    except Subadmin.DoesNotExist:
        return redirect('/subadmin/panel/')  
 
    except:
        return redirect('/subadmin/panel/') 

def new_order(request):
    try:
        subadmin_id = request.session.get('Sub_admin_id')
        admin = Subadmin.objects.get(Sub_admin_id=subadmin_id)
        orders = Order.objects.filter(Sub_admin=subadmin_id, order_status='New').order_by('-id')
        print('new orderrrrrrrr',orders)
        data={
            'suborders': orders, 
                
                'orders_count':suball_count(request),
                'new_orders_count':subnew_count(request),
                'ship_orders_count':subship_count(request),
                'ready_orders_count':subready_count(request),
                'deliver_orders_count':subdeliver_count(request),
                'cancel_orders_count':subcancel_count(request),
                'failed_orders_count':Order.objects.filter(Sub_admin=subadmin_id, order_status='Failed').count()
        }
        return render (request,'Subadmin_Orderdetail.html',data)
    except Subadmin.DoesNotExist:
        return redirect('/subadmin/panel/')  
 
    except:
        return redirect('/subadmin/panel/') 


def ready_order(request):
    try:
        subadmin_id = request.session.get('Sub_admin_id')
        admin = Subadmin.objects.get(Sub_admin_id=subadmin_id)
        orders = Order.objects.filter(Sub_admin=subadmin_id, order_status='ready').order_by('-id')
        print('ready orderrrrrrrr',orders)
        data={
            'suborders': orders, 
                
                'orders_count':suball_count(request),
                'new_orders_count':subnew_count(request),
                'ship_orders_count':subship_count(request),
                'ready_orders_count':subready_count(request),
                'deliver_orders_count':subdeliver_count(request),
                'cancel_orders_count':subcancel_count(request),
                'failed_orders_count':Order.objects.filter(Sub_admin=subadmin_id, order_status='Failed').count()
        }
        return render (request,'Subadmin_Orderdetail.html',data)
    
    except Subadmin.DoesNotExist:
        return redirect('/subadmin/panel/')  
 
    except:
        return redirect('/subadmin/panel/') 



def shipped_order(request):
    try:
        subadmin_id = request.session.get('Sub_admin_id')
        admin = Subadmin.objects.get(Sub_admin_id=subadmin_id)
        orders = Order.objects.filter(Sub_admin=subadmin_id, order_status='shipped').order_by('-id')
        print('new orderrrrrrrr',orders)
        data={
            'suborders': orders, 
                
                'orders_count':suball_count(request),
                'new_orders_count':subnew_count(request),
                'ship_orders_count':subship_count(request),
                'ready_orders_count':subready_count(request),
                'deliver_orders_count':subdeliver_count(request),
                'cancel_orders_count':subcancel_count(request),
                'failed_orders_count':Order.objects.filter(Sub_admin=subadmin_id, order_status='Failed').count()
        }
        return render (request,'Subadmin_Orderdetail.html',data)
    
    except Subadmin.DoesNotExist:
        return redirect('/subadmin/panel/')  
 
    except:
        return redirect('/subadmin/panel/') 




def deliver_order(request):
    try:
        subadmin_id = request.session.get('Sub_admin_id')
        admin = Subadmin.objects.get(Sub_admin_id=subadmin_id)
        orders = Order.objects.filter(Sub_admin=subadmin_id, order_status='delivered').order_by('-id')
        print('new orderrrrrrrr',orders)
        data={
            'suborders': orders, 
                
                'orders_count':suball_count(request),
                'new_orders_count':subnew_count(request),
                'ship_orders_count':subship_count(request),
                'ready_orders_count':subready_count(request),
                'deliver_orders_count':subdeliver_count(request),
                'cancel_orders_count':subcancel_count(request),
                'failed_orders_count':Order.objects.filter(Sub_admin=subadmin_id, order_status='Failed').count()
        }
        return render (request,'Subadmin_Orderdetail.html',data)
    except Subadmin.DoesNotExist:
        return redirect('/subadmin/panel/')  
 
    except:
        return redirect('/subadmin/panel/') 
    

def cancel_order(request):
    try:
        subadmin_id = request.session.get('Sub_admin_id')
        admin = Subadmin.objects.get(Sub_admin_id=subadmin_id)
        orders = Order.objects.filter(Sub_admin=subadmin_id, order_status='canceled').order_by('-id')

        print('new orderrrrrrrr',orders)
        data={
            'suborders': orders, 
                
                'orders_count':suball_count(request),
                'new_orders_count':subnew_count(request),
                'ship_orders_count':subship_count(request),
                'ready_orders_count':subready_count(request),
                'deliver_orders_count':subdeliver_count(request),
                'cancel_orders_count':subcancel_count(request),
                'failed_orders_count':Order.objects.filter(Sub_admin=subadmin_id, order_status='Failed').count()

        }
        return render (request,'Subadmin_Orderdetail.html',data)
    except Subadmin.DoesNotExist:
        return redirect('/subadmin/panel/')  
 
    except:
        return redirect('/subadmin/panel/') 
    
def failed_order(request):
    try:
        subadmin_id = request.session.get('Sub_admin_id')
        admin = Subadmin.objects.get(Sub_admin_id=subadmin_id)
        orders = Order.objects.filter(Sub_admin=subadmin_id, order_status='Failed').order_by('-id')

        print('new orderrrrrrrr',orders)
        data={
            'suborders': orders, 
                
                'orders_count':suball_count(request),
                'new_orders_count':subnew_count(request),
                'ship_orders_count':subship_count(request),
                'ready_orders_count':subready_count(request),
                'deliver_orders_count':subdeliver_count(request),
                'cancel_orders_count':subcancel_count(request),
                'failed_orders_count':Order.objects.filter(Sub_admin=subadmin_id, order_status='Failed').count()
        }
        return render (request,'Subadmin_Orderdetail.html',data)
    except Subadmin.DoesNotExist:
        return redirect('/subadmin/panel/')  
 
    except:
        return redirect('/subadmin/panel/')     



###########################################################################################################

def accept_order(request):
    try:
        subadmin_id = request.session.get('Sub_admin_id')
        admin = Subadmin.objects.get(Sub_admin_id=subadmin_id)
        Order_i = request.GET['idd']
        order= Order.objects.get(order_id = Order_i)
   
        order.order_status = "ready"
        order.save() 
 
        return redirect('/subadmin/panel/ready_orders/')
        # return HttpResponse('accept Order successfully')

    except Subadmin.DoesNotExist:
        return redirect('/subadmin/panel/')  
 
    except:
        return redirect('/subadmin/panel/')     



def subadmin_ship_orders(request):
    try:
        subadmin_id = request.session.get('Sub_admin_id')
        admin = Subadmin.objects.get(Sub_admin_id=subadmin_id)
        if request.method == 'GET':
            Order_i = request.GET.get('idd')
            tracking_link = request.GET.get('Link')
            tracking_id = request.GET.get('Tracking_id')

            order= Order.objects.get(order_id = Order_i)
                    
            order.order_status = 'shipped'
            order.tracking_link = tracking_link
            order.tracking_id = tracking_id

                
            order.save()
            return redirect('/subadmin/panel/shipped_orders/')    
            # return HttpResponse('Shipped Order successfully')

    except Subadmin.DoesNotExist:
        return redirect('/subadmin/panel/')  
 
    except:
        return redirect('/subadmin/panel/')     



def subadmin_deliver_orders(request):
    try:
        subadmin_id = request.session.get('Sub_admin_id')
        admin = Subadmin.objects.get(Sub_admin_id=subadmin_id)
        if request.method == 'GET':
                Order_i = request.GET.get('Deliver')
                print(f"Order ID to deliver: {Order_i}")

                order= Order.objects.get(order_id = Order_i)

            
                order.order_status = 'delivered'
                order.save()
                # return HttpResponse('Deliver order successfully')
                
                return redirect('/subadmin/panel/deliver_orders/')
    except Subadmin.DoesNotExist:
        return redirect('/subadmin/panel/')  
 
    except:
        return redirect('/subadmin/panel/') 
   


def subadmin_cancel_orders(request):
    try:
        subadmin_id = request.session.get('Sub_admin_id')
        admin = Subadmin.objects.get(Sub_admin_id=subadmin_id)
        if request.method == 'GET':
                Order_i = request.GET.get('Cancel')
                print(f"Order ID to cancel: {Order_i}")

                order= Order.objects.get(order_id = Order_i)
                order.order_status = 'canceled'
                order.save()
                # return HttpResponse('  orders cancel successfully')
                return redirect('/subadmin/panel/cancel_orders/')
            
        # return HttpResponse('cancel Order successfully')

    except Subadmin.DoesNotExist:
        return redirect('/subadmin/panel/')  
 
    except:
        return redirect('/subadmin/panel/')     
    


###########################################  PAYMENT START #############################################   

def payment(request):
    try:
        subadmin_id = request.session.get('Sub_admin_id')
        admin = Subadmin.objects.get(Sub_admin_id=subadmin_id)
        # all_payments = Order.objects.all()  
        all_ord = Order.objects.filter(Sub_admin=subadmin_id)
        print('all_orddddddddddddddddddddddddddddddd',all_ord)
        return render(request, 'subadmin_payment.html', {'payments': all_ord})
    except Subadmin.DoesNotExist:
        return redirect('/subadmin/panel/')  
 
    except:
        return redirect('/subadmin/panel/') 

from django.shortcuts import render, get_object_or_404


def payment_detail(request, order_id):
    try:
            subadmin_id = request.session.get('Sub_admin_id')
            admin = get_object_or_404(Subadmin, Sub_admin_id=subadmin_id)
            order = get_object_or_404(Order, order_id=order_id, Sub_admin=subadmin_id)

            return render(request, 'subadmin_payment_detail.html', {'payment': order})
        
    except Subadmin.DoesNotExist:
        return redirect('/subadmin/panel/')  
 
    except:
        return redirect('/subadmin/panel/')  

      
    # except Subadmin.DoesNotExist:
    #     return redirect('/subadmin/panel/')  
 
    # except:
    #     return redirect('/subadmin/panel/') 


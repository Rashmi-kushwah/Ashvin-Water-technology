"""
URL configuration for Eeurekaforbes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.urls import path , include

from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [

    path('admin/panel/', include('Admin.urls')),
    path('Subadmin/panel/', include('Subadmin.urls')),
    path('admin/', admin.site.urls),
    
    path('', views.home, name=''),
    path('login/', views.user_login, name='login'),
    path('header', views.header, name='header'),
    path('footer', views.footer, name='footer'),
    path('Slider', views.Slider, name='Slider'),
    path('profiles/',views.profile,name='profile'), 
    path('register/',views.register),
    path('otp/verify/',views.otp_verify),
    path('otp/',views.otp),
    path('forgot_password/',views.forgot_password, name='forgot_password'),
    path('Otp_view/', views.otp_view, name='Otp_view'),
    path('water-purifiers/', views.PRODUCT, name='PRODUCT'),
    path('New_Launchproducts/', views.New_Launchproduct, name='New_Launchproduct'),
    path('Trending_Launchproducts/', views.Trending_Launchproduct, name='Trending_Launchproduct'),
    path('Product_Details/<uuid:Pd_id>/',views.Product_Detail, name='Product_Detail'),
    path('Add_Cart/',views.Adcart,name='Adcart'),
    path('cart/',views.cart,name='cart'),
    path('check_out/',views.check_out,name='check_out'),
    path('cart_count/',views.cart_count,name='cart_count'), 

    path('Main_Category/',views.main_Category,name='main_Category'), 
    # path('Product_Main_Category/',views.ProductMain_Category,name='Product_Main_Category'),
    path('Product_Main_Category/<int:id>/', views.ProductMain_Category, name='Product_Main_Category'),
    path('Product_sub_Category/<int:id>/', views.Productsub_Category, name='Product_sub_Category'),
    path('remove_product/',views.remove_product),
    path('Payments/', views.Payment, name='Payment'),
    path('check_out/',views.check_out,name='check_out'),
    path('update-cart/', views.update_cart, name='update_cart'),
  
    path('Userall_order/', views.user_all_order, name='user_all_order'),
    path('UserNew_order/', views.user_new_order, name='user_new_order'),
    path('UserShipped_order/', views.user_shipped_order, name='user_shipped_order'),
    path('UserDeliver_order/', views.user_delivered_order, name='user_delivered_order'),
    path('UserReady_order/', views.user_ready_order, name='user_ready_order'),
    path('UserCancel_order/', views.user_cancel_order, name='user_cancel_order'),
    
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

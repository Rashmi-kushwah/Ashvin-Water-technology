

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

app_name = 'Subadmin'

urlpatterns = [
    path('', views.Subadmin_login, name=''),
    path('subadmin_dashboard/', views.Sub_Dashboard, name='Sub_dashboard'),
    path('subadmin_order/', views.Subadmin_orders, name='Subadmin_orders') ,
    path('subadmin_addproducts/', views.subadmin_addproduct, name='subadmin_addproduct'),
    path('subadmin_add-main-category/', views.subadmin_add_main_category, name='subadmin_add_main_category'),
    path('subadmin_add-sub-category/', views.subadmin_add_sub_category, name='subadmin_add_sub_category'),
    path('subadmin_Inventory/', views.subadmin_inventory, name='subadmin_inventory'), 
    path('subadmin_payment/', views.payment,name='payment' ),
    path('subadmin_payment_Detail/<str:order_id>/', views.payment_detail, name='payment_detail'),

    path('subadmin_Edit_product/', views.subadmin_edit_product, name='subadmin_edit_product'),

  
    path('subadmin_Active_product/', views.subadmin_active_product,name='subadmin_active_product' ),
    path('subadmin_Inactive_product/', views.subadmin_inactive_product,name='subadmin_inactive_product' ),
    path('subadmin_Outof_Stock/', views.subadmin_Outof_Stock, name='subadmin_Outof_Stock'),
    path('subadmin_In_Stock/', views.subadmin_In_Stock, name='subadmin_In_Stock'),

    path('all_orders/', views.all_order, name='all_order'), 
    path('new_orders/', views.new_order, name='new_order') ,
    path('ready_orders/', views.ready_order, name='ready_order') ,
    path('shipped_orders/', views.shipped_order, name='shipped_order') ,
    path('deliver_orders/', views.deliver_order, name='deliver_order'),
    path('cancel_orders/', views.cancel_order, name='cancel_order'),
    path('failed_orders/', views.failed_order, name='failed_order'),
   

    path('accept_order/',views.accept_order,name='accept_order'),
    path('subadmin_ship_order/', views.subadmin_ship_orders, name='subadmin_ship_orders'),
    path('subadmin_deliver_order/', views.subadmin_deliver_orders, name='subadmin_deliver_order'),  
    path('subadmin_Cancel_order/',views.subadmin_cancel_orders,name='subadmin_cancel_orders'),
    
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

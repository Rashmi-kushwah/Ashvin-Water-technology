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

app_name = 'Admin'

urlpatterns = [
 #   path('admin/', admin.site.urls),
    path('', views.admin_login, name=''),
    path('dashboard/', views.Dashboard, name='dashboard'), 
    path('orders/', views.orders,name='orders' ),
    # path('payment/', views.payment,name='payment' ),
    # path('payment/<int:customer_id>/', views.payment_detail, name='payment_detail'),
    path('header/', views.admin_header,name='admin_header' ),
    path('Add_product_details/', views.Add_product_detail,name='Add_product_detail' ),
    path('Edit_product/',views.edit_product,name= 'edit_product'),
    path('Edit_banner/',views.edit_banner,name= 'edit_banner'),
    path('Inventory/', views.inventory,name='inventory' ),
    path('Inactive_product/', views.inactive_product,name='inactive_product' ),
    path('Active_product/', views.active_product,name='active_product' ),
    path('Outof_Stock/', views.Outof_Stock, name='Outof_Stock'),
    path('In_Stock/', views.In_Stock, name='In_Stock'),


    path('All_orders/',views.all_orders,name='all_orders'),
    path('New_orders/',views.new_orders,name='new_orders'),
    path('Shipped_orders/',views.shipped_orders,name='Shipped_orders'),

    path('Deliver_orders/',views.deliver_orders,name='deliver_orders'),
    path('Ready_orders/',views.ready_orders,name='ready_orders'),
    path('Cancel_orders/',views.cancel_orders,name='cancel_orders'),
    path('Accept_order/',views.accept_order,name='accept_order'),
    path('admin_Ship_order/',views.admin_ship_order,name='admin_ship_order'),
    path('admin_Cancel_order/',views.admin_cancel_order,name='admin_cancel_order'),
    path('admin_deliver_order/',views.admin_deliver_order,name='admin_deliver_order'),



    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


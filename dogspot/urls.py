"""dogspot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include
from applications import views
import customer
from django.conf.urls import url
from applications.views import HomeView,ProjectChart

urlpatterns = [
    path('admin/', admin.site.urls),

    #  client url+++++++++++++++++++++++++++++++++++++++++++++ 
    path('client/',include('customer.urls')),
    
   # graph====================================================================
    url(r'charthome',HomeView.as_view(),name='home'),
    url(r'^api/chart/data/$',ProjectChart.as_view(),name='api-data'),

    # =SELETE q=================
    path('user-table/',views.user_table),
    path('state-table/',views.state_table),
    path('city-table/',views.city_table),
    path('area-table/',views.area_table),
    path('category-table/',views.category_table),
    path('sub-category-table/',views.sub_category_table),
    path('product-table/',views.product_table),
    path('payment-table/',views.payment_table),
    path('order-table/',views.order_table),
    path('wishlist-table/',views.wishlist_table),
    path('appect-order/<int:orders_id>/',views.appect_order),
    path('reject-order/<int:orders_id>/',views.reject_order),

    path('gallery-table/',views.gallery_table),
    path('docter-table/',views.docter_table),
    path('order-item-table/<int:orders_id>/',views.order_items_table),
    path('feedback-table/',views.feedback_table),

# Log in url===========================================
    path('admin-login/',views.admin_login),
    path('forgot/',views.forgot),   
    path('send-mail/',views.send_OTP),
    path('set/',views.set_password),
    path('admin-logout/',views.alogout),

# delete column urlss-----------------------------------
    path('delete-state/<int:states_id>/',views.delete_state),
    path('delete-city/<int:citys_id>/',views.delete_city),
    path('delete-area/<int:areas_id>/',views.delete_area),
    path('delete-category/<int:categorys_id>/',views.delete_category),
    path('delete-sub-category/<int:sub_categorys_id>/',views.delete_sub_category),
    path('delete-product/<int:products_id>/',views.delete_product),
    path('delete-payment/<int:payments_id>/',views.delete_payment),
    path('delete-order/<int:orders_id>/',views.delete_order),
    path('delete-gallery/<int:gallerys_id>/',views.delete_gallery),
    path('delete-docter/<int:docters_id>/',views.delete_docter),
    path('delete-order-itme/<int:order_items_id>/',views.delete_order_item),
    path('delete-feedback/<int:feedbacks_id>/',views.delete_feedback),
   
#    Insert data================================================
    path('insert-category/',views.insert_category),
    path('insert-sub-category/',views.insert_sub_category),
    path('insert-state/',views.insert_state),
    path('insert-city/',views.insert_city),
    path('insert-area/',views.insert_area),
    path('insert-docter/',views.insert_docter),
    path('insert-gallery/',views.insert_gallery),
    path('insert-product/',views.insert_product),
    #  update  data==================================================
    path('edit-state/<int:states_id>',views.eidt_state),
    path('update-state/<int:states_id>',views.update_state),
    path('edit-city/<int:citys_id>',views.edit_city),
    path('update-city/<int:citys_id>',views.update_city),
    path('edit-area/<int:areas_id>',views.edit_area),
    path('update-area/<int:areas_id>',views.update_area),
    path('edit-category/<int:categorys_id>',views.edit_category),
    path('update-category/<int:categorys_id>',views.update_categorys),
    path('edit-sub-category/<int:sub_categorys_id>',views.edit_sub_category),
    path('update-sub-category/<int:sub_categorys_id>',views.update_sub_category),
    path('edit-product/<int:products_id>',views.edit_product),
    path('update_product/<int:products_id>',views.update_product),
    path('edit_docter/<int:docters_id>',views.edit_docter),
    path('update_docter/<int:docters_id>',views.update_docter),
    path('edit_gallery/<int:gallerys_id>',views.edit_gallery),
    path('update_gallery/<int:gallerys_id>',views.update_gallery),

    path('profile/',views.edit_profile),
    path('update-profile/',views.update_profile),
    path('header/',views.header),
    path('',views.client),

    # ropost========================
    path('order_repost/',views.order_repost),
    path('repost2/',views.repost2),
    path('repost3/',views.repost3),
    
    path('index/',views.index),
]

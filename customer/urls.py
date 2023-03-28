from django.urls import path
from django.contrib import admin
from  customer import c_views


urlpatterns = [
    
    path('login/',c_views.login),
    path('register/',c_views.register), 
    path('forgot/',c_views.forgot), 
    path('send-otp/',c_views.send_otp), 
    path('c-set/',c_views.set_password),
    path('clogout/',c_views.clogout),
    path('client_header_menu/',c_views.load_menu),
    path('cart_menu/',c_views.cart_menu),
    path('update_c_profile/',c_views.update_c_profile),
    path('pass_change/',c_views.pass_change),

    path('sidebar_shop/',c_views.sidebar), 
    path('select_sub_category/<int:sub_categorys_id>/',c_views.select_sub_category),
    
    path('home/',c_views.home),
    path('cart/',c_views.cart_),
    path('select_category/<int:categorys_id>/',c_views.select_category),
    path('wishlist/',c_views.wishlist),
    path('int_wishlist/',c_views.int_wishlist),
    path('wishlist_delete/<int:wishlists_id>/',c_views.wishlist_delete),
    path('docters/',c_views.docter_details),
    path('product-details/<int:products_id>/',c_views.product_details),
    path('checkout/',c_views.checkout),
    path('account/',c_views.c_profile),
    path('feedback/<int:products_id>/',c_views.feedback),
    path('insert_cart/<int:products_id>/',c_views.insert_cart),

    path('delete_cart/<int:id>/',c_views.destroy_cart),
    path('clear_cart/',c_views.clear_cart),

    path('add_wishlist/<int:id>/',c_views.add_wishlist),

    path('search/',c_views.autosuggest,name='search1'),
    path('sort_porduct/',c_views.sort_products),
    path('payments/<int:total>/',c_views.select_checkout),

    path('cancel/',c_views.cancel),
    path('select_payment/<int:total>',c_views.select_payment),
    path('order/',c_views.order_),
    path('order_details/<int:orders_id>/',c_views.order_details),
    path('update_cart/<int:id>',c_views.update_cart),
    path('filter_price/',c_views.filter_price),
]
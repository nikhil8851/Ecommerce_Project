from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('base',views.base , name='base'),
    path('product_detail/<slug:slug>',views.product_detail,name='product_detail'),
    path('404', views.error404, name ='404'),
    path('account/my-account', views.my_account,name="my_account"),
    
    
    # this is url path disabel after enabel django registration template
    path('account/register',views.register,name='hregister'),
    path('account/login', views.log, name='hlogi'),
    # end
    path('account/profile', views.profile,name='profile'),
    path('profile/update', views.profile_update,name='profile_update'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('about', views.about, name = 'about'),
    path('contact_us', views.contact, name = 'contact'),
    path('product_main', views.product_main, name='product_main'),
    path('product/filter-data',views.filter_data,name="filter-data"),


    # cart path start
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),
    # cart path end

    
    
]

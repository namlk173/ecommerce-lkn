from django.contrib import admin
from django.urls import URLPattern, path
from . import views


urlpatterns = [
    path('', views.Home, name= 'home'),
    path('login/', views.Login, name='login'),
    path('register/', views.registerPage, name="register"),
    path('logout/', views.Logout, name='logout'),
    path('manage-product/', views.ManagerProduct, name='manage-product'),
    path('delete-product/<str:pk>/', views.DeleteProduct, name='delete-product'),
    path('create-product/<str:CategoryId>', views.createProduct, name='create-product'),
    path('update-product/<str:CategoryId>/<str:pk>/', views.updateProduct, name='update-product'),
    path('order-product/<str:CategoryId>/<str:pk>/', views.orderProduct, name='order-product'),
    path('manage-order/', views.manageOrder, name='manage-order'),
    path('cart/', views.cart, name='cart'),
    path('delete-order/<str:cartId>/<orderId>/', views.deleteOrder, name='delete-order'),
    path('update-infor-delivery/', views.updateInforDelivery, name='update-infor-delivery')
]
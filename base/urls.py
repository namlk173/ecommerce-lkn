from django.urls import URLPattern, path
from . import views


urlpatterns = [
    path('', views.Home, name= 'home'),
    path('login/', views.Login, name='login'),
    path('register/', views.registerPage, name="register"),
    path('logout/', views.Logout, name='logout'),
    path('manage/', views.Manager, name='manage'),
    path('delete-product/<str:pk>/', views.DeleteProduct, name='delete-product'),
    path('create-product/<str:CategoryId>/', views.createProduct, name='create-product'),
    path('update-product/<str:CategoryId>/<str:pk>/', views.updateProduct, name='update-product'),
    path('order-product/<str:CategoryId>/<str:pk>/', views.orderProduct, name='order-product'),
    path('buy-now/<str:pk>/', views.buyNow, name='buy-now'),
    path('manage-order/', views.manageOrder, name='manage-order'),
    path('cart/', views.cart, name='cart'),
    path('delete-order/<orderId>/', views.deleteOrder, name='delete-order'),
    path('choose-address-delivery/', views.chooseAddressDelivery, name='choose-address-delivery'),
    path('update-address-delivery/<str:pk>/', views.updateAddressDelivery, name='update-address-delivery'),
    path('address-address-delivery/', views.addAdressDelivery, name='add-address-delivery'),
    path('delete-address-delivery/<str:pk>/', views.deleteAddressDelivery, name='delete-address-delivery'),
    path('view-order/', views.viewOrder, name='view-order'),
    path('write-comment/<str:categoryID>/<str:productID>', views.write_comment, name='write-comment'),
    path('process-payment/', views.process_payment, name='process-payment'),
    path('payment-done/', views.payment_done, name='payment-done'),
    path('payment-cancel/', views.payment_cancel, name='payment-cancel'),
]
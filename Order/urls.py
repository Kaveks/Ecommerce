from django.urls import path
from . import views


app_name="Order"

urlpatterns = [
     path("add-to-cart/<slug>", views.addToCart, name="add-to-cart"),
    path("remove-from-cart/<slug>", views.removeFromCart, name="remove-from-cart"),
    path("remove-item-from-cart/<slug>/",views.removeSingleItemFromCart,
            name="remove-single-item-from-cart"),
    path("move-item-to-cart/<slug>/", views.moveToCart,name='move-item-to-cart'),
    path("order-summary/", views.OrderSummaryView.as_view(), name="order-summary"),
     path("orders/", views.CustomerOrderView.as_view(), name="orders"),
    path("checkout/", views.CheckoutView.as_view(), name="checkout"),
    path("add-coupon/", views.AddCouponView.as_view(), name="add-coupon"),
    path("payment1/<payment_option>/", views.StripePaymentView.as_view(), name="payment1"),
    path("payment2/<payment_option>/", views.PaypalPaymentView.as_view(), name="payment2"),
    path("paypal_payment_complete/", views.paypalPaymentComplete, name="paypal_complete"),
    path("request-refund/", views.RequestRefundView.as_view(), name="request-refund"),
]

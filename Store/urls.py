from django.urls import path
from . import views


app_name="Store"

urlpatterns = [
    path("",views.HomeView.as_view(), name="home"),
    path("product/<slug>/", views.ItemView.as_view(), name="product"),
]
from django.shortcuts import render
from django.views.generic import View,ListView,DetailView
from .models import Item

# Create your views here.
class HomeView(ListView):
    model=Item
    template_name="Store/home.html"
    paginate_by=15
    context_object_name="products"


    def get_context_set(self):
        products=Item.objects.filter(stocked=True)
        return products


class ItemView(DetailView):
    model=Item
    template_name="Store/product_detail.html"
    #context_object_name=""


    #def 
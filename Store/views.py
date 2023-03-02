from django.shortcuts import render,get_object_or_404
from django.views.generic import View,ListView,DetailView
from .models import Item,Category

# Create your views here.
class HomeView(ListView):
    model=Item
    template_name="Store/home.html"
    paginate_by=4
    context_object_name="products"


    def get_context_set(self):
        products=Item.objects.filter(stocked=True)
        return products


class ItemView(DetailView):
    model=Item
    template_name="Store/product_detail.html"
    #context_object_name=""
    #def 



def category_list(request,slug):
     category1=get_object_or_404(Category,slug=slug)
     products=Item.objects.filter(category=category1)
     # using mptt category functionality
     #products=Item.objects.filter(category__in=Category.objects.get(name=slug).get_descendants(include_self=True))
     #data=cartData(request)
     #CartItems=data["CartItems"]
     context={'category': category1,'products':products}
     return render(request, 'Store/category.html',context)

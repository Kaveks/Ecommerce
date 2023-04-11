
# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
# from Order.views import userOrders

# Create your views here.
from .forms import RegistrationForm
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from User.token import account_activation_token
from User.models import Account
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# from orders.views import user_orders

from .forms import RegistrationForm, UserEditForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from User.decorators import authenticate_user, allowed_users, admin_only
from Store.models import Item
from Customer.models import Address
from Customer.forms import CustomerAddressForm


@login_required
@allowed_users(allowed_group=['Customer'])
def wishlist(request):
    products = Item.objects.filter(users_wishlist=request.user)
    return render(request, "User/dashboard/user_wishlist.html", {"wishlist_product": products})


@login_required
@allowed_users(allowed_group=['Customer'])
def add_to_wishlist(request, id):
    product = get_object_or_404(Item, id=id)
    if product.users_wishlist.filter(id=request.user.id).exists():
        product.users_wishlist.remove(request.user)
        messages.success(request, product.title +
                         " has been removed from your WishList,"+
                         "through Dashboard go to Home page to add it again")
        return redirect('User:wishlist')
    else:
        product.users_wishlist.add(request.user)
        messages.success(request, "Added " +
                         product.title + " to your WishList see in your Dashboard")
        return redirect('Store:home')
    return HttpResponseRedirect(request.META["HTTP_REFERER"])


@login_required(login_url='User:login')
@allowed_users(allowed_group=['Customer'])
def dashboard(request):
    '''
        order = userOrders(request)
        orders=order['ordered']
        #total=order['total']
        #production=order['production']

        #delivered=order['delivered']
        #on_delivery=order['on_delivery']
        context={ 'orders':orders,


                }
        'production': production,
                'on_delivery':on_delivery,'delivered':delivered 
    '''
    return render(request, 'User/dashboard/customer_dashboard.html')


@login_required
@allowed_users(allowed_group=['Customer'])
def edit_details(request):
    if request.method == 'POST':
        edit_user_form = UserEditForm(instance=request.user, data=request.POST)

        if edit_user_form.is_valid():
            edit_user_form.save()
            return HttpResponseRedirect(reverse("User:dashboard"))
       
    else:
        edit_user_form = UserEditForm(instance=request.user)

    return render(request,
                  'User/user/edit_details.html', {'edit_user_form': edit_user_form})


@login_required
@allowed_users(allowed_group=['Customer'])
def delete_user(request):
    user = Account.objects.get(user_name=request.user)
    user.is_active = False
    user.save()
    logout(request)
    return redirect('User:delete_confirmation')


@authenticate_user
def account_register(request):
    if request.method == 'POST':
        registerForm = RegistrationForm(request.POST)
        if registerForm.is_valid():
            user = registerForm.save(commit=False)
            user.email = registerForm.cleaned_data['email']
            user.set_password(registerForm.cleaned_data['password1'])
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate your Account'
            message = render_to_string('User/registration/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject=subject, message=message)
            return HttpResponse(' Account registered successfully check your email to activate your account ')
    else:
        registerForm = RegistrationForm()
    return render(request, 'User/registration/register.html', {'form': registerForm})


def account_activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = Account.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, user.DoesNotExist):  # type: ignore
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('User:dashboard')
    else:
        return render(request, 'User/registration/activation_invalid.html')


# Addresses

@login_required
@allowed_users(allowed_group=['Customer'])
def view_address(request):
    addresses = Address.objects.filter(customer=request.user)
    return render(request, "User/dashboard/addresses.html", {"addresses": addresses})


@login_required
@allowed_users(allowed_group=['Customer'])
def add_address(request):
    if request.method == "POST":
        address_form = CustomerAddressForm(data=request.POST)
        if address_form.is_valid():
            address_form = address_form.save(commit=False)
            address_form.customer = request.user
            address_form.save()
            return HttpResponseRedirect(reverse("User:view_addresses"))
    else:
        address_form = CustomerAddressForm()
    return render(request, "User/dashboard/edit_addresses.html", {"form": address_form})


@login_required
@allowed_users(allowed_group=['Customer'])
def edit_address(request, id):
    if request.method == "POST":
        address = Address.objects.get(pk=id, customer=request.user)
        address_form = CustomerAddressForm(instance=address, data=request.POST)
        if address_form.is_valid():
            address_form.save()
            return HttpResponseRedirect(reverse("User:view_addresses"))
    else:
        address = Address.objects.get(pk=id, customer=request.user)
        address_form = CustomerAddressForm(instance=address)
    return render(request, "User/dashboard/edit_addresses.html", {"form": address_form})


@login_required
@allowed_users(allowed_group=['Customer'])
def delete_address(request, id):
    address = Address.objects.filter(pk=id, customer=request.user).delete()
    return redirect("User:view_addresses")


@login_required
@allowed_users(allowed_group=['Customer'])
def set_default(request, id):
    address1=Address.objects.filter(customer=request.user, address_type="Shipping")
    address2=Address.objects.filter(customer=request.user, address_type="Shipping")
    if address1.exists():
        Address.objects.filter(pk=id, customer=request.user).update(default=True)
    elif address2.exists():
            Address.objects.filter(pk=id, customer=request.user).update(default=True)
    return redirect("User:view_addresses")


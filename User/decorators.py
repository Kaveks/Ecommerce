from django.http import HttpResponse
from django.shortcuts import redirect


# register and login pages user authentication check up
# whichever function referenced by decorator is what is passed here as view_func
def authenticate_user(view_func):
    def wrapper_function(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('User:dashboard')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_function



def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_function(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                if group in allowed_roles:
                    return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not authorized to view this page')
        return wrapper_function
    return decorator

def admin_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group == 'Customer':
            return redirect('User:dashboard')
        if group == 'Staff':
            return view_func(request, *args, **kwargs)
        if group == 'Admin':
            return view_func(request, *args, **kwargs)
        if group == 'Owner':
            return view_func(request, *args, **kwargs)
    return wrapper_function 
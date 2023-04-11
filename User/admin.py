from django.contrib import admin
from . models import Account
from django.contrib.auth.admin import UserAdmin
# Register your models here.


class UserAdminConfig(UserAdmin):
    ordering = ('-created', 'updated',)
    list_display = ('user_name', 'email', 'is_active',
                    'is_staff', 'is_superuser')
    search_fields = ['user_name', 'email']
    list_filter = ['user_name', 'email', 'is_staff', 'is_superuser']
    fieldsets = (
        (None, {'fields': ('user_name', 'email', 'password')}),
        ('Personal Information', {'fields': ('first_name','last_name', 'phone',)}),
         ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                    'groups')}),
           # ('Time',{'fields':('created','updated')}),
         ('Timelines', {'fields': ('created', 'updated', 'last_login')})
        # ('Residency',{'fields':(''')})
    )
    # formfield_overrides={
    # UserBase.about:{'widget':Textarea(attrs={'rows':10,'cols':40})},
    # }
    add_fieldsets = ((None, {
        'classes': ('wide',),
        'fields': ('email', 'user_name', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser',),
    }),)


admin.site.register(Account, UserAdminConfig)

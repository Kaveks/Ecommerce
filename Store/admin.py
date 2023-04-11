from django.contrib import admin
from . models import (Item, Category, Item_Image1,
                      Item_Image2, Item_Image3, Item_Image4)

from django.forms import TextInput, Textarea
from django.db import models
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',), }
    fieldsets = (('None', {'fields': ('name', 'slug')}),
                 )


class Item_Image1Inline(admin.TabularInline):
    model = Item_Image1
    extra = 0


class Item_Image2Inline(admin.TabularInline):
    model = Item_Image2
    extra = 0


class Item_Image3Inline(admin.TabularInline):
    model = Item_Image3
    extra = 0


class Item_Image4Inline(admin.TabularInline):
    model = Item_Image4
    extra = 0


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',), }
    ordering = ('-updated',)
    list_display = ('title', 'sub_category', 'updated')
    list_filter = ['sub_category']
    # add a search button
    search_fields = ['sub_category']
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'30'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':50})},
    }
    fieldsets = (
        ('Category', {'fields': ('category', 'sub_category',)}),
        ('Main', {'fields': ('title', 'slug', 'price', 'discount_price', 'label')}),

        # ('Time',{'fields':('created','updated')}),
        ('More Details', {'fields': ('stocked',
         'digital', 'updated', 'description','additional_info')}),
        ('Wishlist',{'fields':('users_wishlist',)}),
    )
    inlines = [Item_Image1Inline, Item_Image2Inline,
               Item_Image3Inline,Item_Image4Inline]

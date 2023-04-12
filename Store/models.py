from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
import datetime
from django.urls import reverse
from User.models import Account
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True, null=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name="Category"
        verbose_name_plural = 'Categories'
        ordering=("-name",)
        

    def get_absolute_url(self):
        return reverse('Store:category', args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)


category_choices = (
    ("S", "Shirt"),
    ("Sp", "Sport wear"),
    ("OW", "Out wear"),
    ("PH", "Phone"),
    ("SH", "Shoes"),
)

label_choices = (("P", "primary"), ("S", "secondary"), ("D", "danger"))


class Item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    sub_category=models.CharField(max_length=4, choices=category_choices, null=True)
    title = models.CharField(max_length=255, verbose_name=_(
        'Title'), help_text=_('Required'), null=True)
    slug = models.SlugField(max_length=255, verbose_name=_('Slug'),
                              help_text=_('Required'), null=True)
    price = models.DecimalField(max_digits=9, verbose_name=_(
        'Price'), help_text=_('Required'), decimal_places=2, null=True)
    discount_price = models.DecimalField(max_digits=9, verbose_name=_(
        'Discount price'), blank=True, decimal_places=2, null=True)
    stocked = models.BooleanField(default=True, verbose_name=_('is_stock'))
    digital = models.BooleanField(
        default=False, verbose_name=_('is_digital'), null=True, blank=True)
    now = timezone.make_aware(datetime.datetime.now(),
                              timezone.get_default_timezone())
    updated = models.DateTimeField(
        default=now, verbose_name=_('Updated at'))
    discount_price = models.FloatField(blank=True, null=True)
    label = models.CharField(max_length=2,verbose_name=_('Label color'),default=label_choices[2] ,choices=label_choices, null=True)
    description = models.TextField(verbose_name=_(
        'Description'), help_text=_('optional(briefly say about the product)'), blank=True, null=True)
    additional_info = models.TextField(verbose_name=_(
        'Additional Information'), help_text=_('optional(applicable when adding Second-Fourth Images)'), blank=True, null=True)
    users_wishlist = models.ManyToManyField(Account, related_name="user_wishlist", blank=True)

    class Meta:
        verbose_name = _('Item')
        verbose_name_plural = _('Items')
        ordering = ('-updated',)


    def get_absolute_url(self):
        return reverse("Store:product", args=[self.slug])

    def get_add_to_cart_url(self):
        return reverse("Order:add-to-cart", args=[self.slug])
    
    def get_move_item_to_cart_url(self):
        return reverse("Order:move-item-to-cart", args=[self.slug])

    def get_remove_from_cart_url(self):
        return reverse("Order:remove-from-cart", args=[self.slug])



    def __str__(self):
        return "{} {}".format(self.title,self.updated)


class Item_Image1(models.Model):
    ''' The product image table'''
    item = models.ForeignKey(
        Item, related_name='image1', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/%y/%m', verbose_name=_('Image'),
                              help_text=_("Upload Item's image"), null=True, blank=True)
    Show = models.BooleanField(default=True, verbose_name=_('show'))
    now = timezone.make_aware(datetime.datetime.now(),
                              timezone.get_default_timezone())
    updated = models.DateTimeField(
        default=now, verbose_name=_('created at'), editable=False)

    class Meta:
        verbose_name = _('First Image')
        verbose_name_plural = _('First Image')
        ordering=("-updated",)
    @property
    def ImageUrl(self):
        try:
            url = self.image.url
        except:
            url = ""

        return url


class Item_Image2(models.Model):
    ''' The product image table'''
    item = models.ForeignKey(
        Item, related_name='image2', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/%y/%m', verbose_name=_('Image'),
                              help_text=_("Upload Item's image"), null=True, blank=True)
    Show = models.BooleanField(default=False, verbose_name=_('show'))
    now = timezone.make_aware(datetime.datetime.now(),
                              timezone.get_default_timezone())
    updated = models.DateTimeField(
        default=now, verbose_name=_('created at'), editable=False)

    class Meta:
        verbose_name = _('Second Image')
        verbose_name_plural = _('Second Image')
        ordering=("-updated",)

    @property
    def ImageUrl(self):
        try:
            url = self.image.url
        except:
            url = ""

        return url


class Item_Image3(models.Model):
    ''' The product image table'''
    item = models.ForeignKey(
        Item, related_name='image3', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/%y/%m', verbose_name=_('Image'),
                              help_text=_("Upload Item's image"), null=True, blank=True)
    Show = models.BooleanField(default=False, verbose_name=_('show'))
    now = timezone.make_aware(datetime.datetime.now(),
                              timezone.get_default_timezone())
    updated = models.DateTimeField(
        default=now, verbose_name=_('created at'), editable=False)

    class Meta:
        verbose_name = _('Third Image')
        verbose_name_plural = _('Third Image')
        ordering=("-updated",)

    @property
    def ImageUrl(self):
        try:
            url = self.image.url
        except:
            url = ""

        return url


class Item_Image4(models.Model):
    ''' The product image table'''
    item = models.ForeignKey(
        Item, related_name='image4', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/%y/%m', verbose_name=_('Image'),
                              help_text=_("Upload Item's image"), null=True, blank=True)
    Show = models.BooleanField(default=False, verbose_name=_('show'))
    now = timezone.make_aware(datetime.datetime.now(),
                              timezone.get_default_timezone())
    updated = models.DateTimeField(
        default=now, verbose_name=_('created at'), editable=False)

    class Meta:
        verbose_name = _('Fourth Image')
        verbose_name_plural = _('Fourth Image')
        ordering=("-updated",)

    @property
    def ImageUrl(self):
        try:
            url = self.image.url
        except:
            url = ""

        return url
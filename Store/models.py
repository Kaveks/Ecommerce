from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
import datetime
from django.urls import reverse
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True, null=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('store:category', args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)


tag_choices = (
    ("S", "Shirt"),
    ("Sp", "Sport wear"),
    ("OW", "Out wear"),
    ("PH", "Phone"),
    ("SH", "Shoes"),
)

label_choices = (("P", "primary"), ("S", "secondary"), ("D", "danger"))


class Item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    tags_color = models.CharField(
        max_length=255, default=label_choices[2], choices=tag_choices, null=True)
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
        default=now, verbose_name=_('Updated at'), editable=False)
    discount_price = models.FloatField(blank=True, null=True)
    label = models.CharField(max_length=2,verbose_name=_('Labels'), choices=label_choices, null=True)
    description = models.TextField(verbose_name=_(
        'Description'), help_text=_('optional'), blank=True, null=True)
    # users_wishlist = models.ManyToManyField(User, related_name="user_wishlist", blank=True)

    class Mete:
        verbose_name = _('Item')
        verbose_name_plural = _('Items')
        ordering = ('-updated',)


class Item_Image(models.Model):
    ''' The product image table'''
    item = models.ForeignKey(
        Item, related_name='item_image', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/%y/%m', verbose_name=_('Image'),
                              help_text=_("Upload Item's image"), null=True, blank=True)
    main_pic = models.BooleanField(default=False, verbose_name=_('main image'))
    other_pic1 = models.BooleanField(default=False, verbose_name=_('Img2'))
    other_pic2 = models.BooleanField(default=False, verbose_name=_('Img3'))
    other_pic3 = models.BooleanField(default=False, verbose_name=_('Img4'))
    other_pic4 = models.BooleanField(default=False, verbose_name=_('Img5'))
    now = timezone.make_aware(datetime.datetime.now(),
                              timezone.get_default_timezone())
    updated = models.DateTimeField(
        default=now, verbose_name=_('created at'), editable=False)

    class Meta:
        verbose_name = _('Image')
        verbose_name_plural = _('Images')
        ordering=("-updated")

    @property
    def ImageUrl(self):
        try:
            url = self.image.url
        except:
            url = ""

        return url

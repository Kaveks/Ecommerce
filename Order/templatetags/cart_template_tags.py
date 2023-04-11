from django import template
from Order.models import Order

# register our custom template tag 
register = template.Library()

''' re-run the server again after the tag definition 
    otherwise an error will show on the browser'''

@register.filter
#define a function which is now the name of template tag
def cart_item_count(user):
    #display cart total for only authenticated users
    if user.is_authenticated:
        # define query set
        qs =Order.objects.filter(user=user,ordered=False)
        # check if the order exists
        if qs.exists():
            # return the initial order and count the items
            return qs[0].items.count()
    # otherwise return zero value
    return 0


# load the tag on navbar  with the tag name of the python file
# being the name of the tag load  while to show totals ,
# place  'request.user| name of the above function which happens to be the tag name'

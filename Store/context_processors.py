from Store.models import Category


# this does not require to be in url
# so include the dictionary key in the Templates from settings
#This makes it accessible on every web page
def categories(request):
    return {'categories':Category.objects.all()}

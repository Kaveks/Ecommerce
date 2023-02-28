from django.db.models.signals import post_save
from User.models import Account
from django.contrib.auth.models import Group


from Customer.models import Customer
'''use django signals to create customer  instance into Customer
from Account data and add him/her to group'''
#@receiver(post_save, sender=UserBase)
#def create_customer(sender,instance,created,**kwargs):
    #if created:
    #group = Group.objects.get(name='Customer')
		#instance.groups.add(group)
        #Customer.objects.create(user=instance,name=instance.user_name,email=instance.email)
''' Above code is same as the following'''
def create_customer_and_add_to_group(sender, instance, created, **kwargs):
	if created:
     # check if group Customer exists
		group = Group.objects.get(name='Customer')
		# add customer to the group Customer if created
		instance.groups.add(group)
		# if customer was not created then create
		Customer.objects.create(
			user=instance,
			name=instance.user_name,
			email=instance.email
			)
		print('Profile created!')
# customer will be created from Account model
post_save.connect(create_customer_and_add_to_group, sender=Account) 
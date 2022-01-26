from django.db import models

# Create your models here.

# An old model:
class Product(models.Model):
	title = models.CharField(default='some_value', blank=False, max_length=120)
	description = models.CharField(default='some_value', blank=False, max_length=120)
	target_price = models.DecimalField(default='some_value', blank=False, decimal_places=2, max_digits=1000)

# class Product(models.Model):
# 	email            = models.CharField(null=False, blank=False, max_length=120) # max_lenght required
# 	customer_skype   = models.CharField(null=False, blank=False, max_length=120)
# 	tittle 		  	 = models.CharField(null=False, blank=False, max_length=120)
# 	quantity      	 = models.DecimalField(
# 										   null=False,
# 										   blank=False,
# 										   decimal_places=0,
# 										   max_digits=4,
# 										   default=50,	
# 										   choices=[(i, i) for i in range(50, 9000, 50)]
# 										   ) # Why decimal not float: https://docs.python.org/3/library/decimal.html#module-decimal
# 	target_price  	 = models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=7) # Why decimal not float: https://docs.python.org/3/library/decimal.html#module-decimal
# 	one_time_request = models.BooleanField(default=None)
# 	constant_need    = models.BooleanField(default=None)
# 	how_soon      	 = models.TextField(null=False, blank=True)

# 	# request_published = models.DateTimeField("date published",auto_now=True) # instead of auto now -> default=datetime.now() for setting date

# 	class Meta: 
# 		"""
# 		it will change the name to plural
# 		in the index column where we have the `Add` button
# 		(in our App)
# 		"""
# 		verbose_name_plural = 'Inquiries' 















		# kod poniżej nie działa bo masz metodę `forms`, trzeba poczytać jak ogarnąć ten temat. 
		# tu masz wiedzę: https://stackoverflow.com/questions/5481713/whats-the-difference-between-django-models-and-forms
		# a kod poniżej ma wszystkie dane, ale tak jak mówie, nie działa:


	# 	class Product(models.Model):
	# email           = models.CharField(
	# 									null=False,
	# 									blank=False, 
	# 									max_length=120,# max_lenght required 
	# 									required=True, 
 #                          				widget=models.TextInput(attrs={'placeholder': 'Company email'})) # https://stackoverflow.com/questions/17308194/is-there-a-way-in-django-to-make-it-so-that-when-a-form-with-initial-text-is-cli/17308242
	# customer_skype  = models.CharField(
	# 									null=False, 
	# 									blank=False, 
	# 									max_length=120, 
 #                          				widget=models.TextInput(attrs={'placeholder': 'We can contact you faster with the Skype'}))
	# tittle 		  	= models.CharField(
	# 									null=False, 
	# 									blank=False, 
	# 									max_length=120, 
	# 									widget=models.TextInput(attrs={'placeholder': 'Game/Card title'}))
	# quantity      	= models.DecimalField(
	# 									   null=False,
	# 									   blank=False,
	# 									   decimal_places=0,
	# 									   max_digits=4,
	# 									   default=50,
	# 									   choices=[(i, i) for i in range(50, 9000, 50)]
	# 									   ) # Why decimal not float: https://docs.python.org/3/library/decimal.html#module-decimal
	# target_price  	= models.DecimalField(
	# 										null=True, 
	# 										blank=True, 
	# 										decimal_places=2, 
	# 										max_digits=7, 
	# 										widget=models.TextInput(attrs={'placeholder': 'If you need to have one'})) # Why decimal not float: https://docs.python.org/3/library/decimal.html#module-decimal
	# one_time      	= models.TextField(
	# 									widget=models.TextInput(attrs={'placeholder': 'If you need just one order'}))
	# e_bool_field    = models.BooleanField(verbose_name = gl('Este é um campo booleano'))#, **choices** = bolean_yes_no)
	# constant_need 	= models.TextField(default="no information")
	# how_soon      	= models.TextField(default="no information")
	# request_published = models.DateTimeField("date published",auto_now=True) # instead of auto now -> default=datetime.now() for setting date

	# class Meta: 
	# 	"""
	# 	it will change the name to plural
	# 	in the index column where we have the `Add` button
	# 	(in our App)
	# 	"""
	# 	verbose_name_plural = 'Inquiries' 
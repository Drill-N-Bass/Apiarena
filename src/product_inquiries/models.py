from django.db import models

from datetime import datetime

# Create your models here.
class ProductInquiry(models.Model):
	email           = models.CharField(null=False, blank=False, max_length=120) # max_lenght required
	tittle 		  	= models.TextField(null=False, blank=False)
	quantity      	= models.DecimalField(
										   null=False,
										   blank=False,
										   decimal_places=0,
										   max_digits=4,
										   default=50,
										   choices=[(i, i) for i in range(50, 9000, 50)]
										   ) # Why decimal not float: https://docs.python.org/3/library/decimal.html#module-decimal
	target_price  	= models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=7) # Why decimal not float: https://docs.python.org/3/library/decimal.html#module-decimal
	one_time      	= models.TextField(default="client didn't provide information, or want constant supply")
	constant_need 	= models.TextField(default="no information")
	how_soon      	= models.TextField(default="no information")
	request_published = models.DateTimeField("date published",auto_now=True) # instead of auto now -> default=datetime.now() for setting date

	class Meta: 
		"""
		it will change the name to plural
		in the index column where we have the `Add` button
		(in our App)
		"""
		verbose_name_plural = 'Inquiries' 
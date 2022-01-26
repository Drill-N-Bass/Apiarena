from django import forms

from .models import Product

# An old model:
class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = [
			'title',
			'description',
			'target_price'
		]


# class ProductForm(forms.ModelForm):
# 	class Meta:
# 		model = Product
# 		fields = [
# 			'email',
# 			'customer_skype',
# 			'tittle',
# 			'quantity',
# 			'target_price',
# 			'one_time_request',
# 			'constant_need',
# 			'how_soon'
# 		]


class RawProductForm(forms.Form):
	title        = forms.CharField()
	description  = forms.CharField()
	target_price = forms.DecimalField()
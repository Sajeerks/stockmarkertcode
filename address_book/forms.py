from django import forms

from .models import Address


class AddressForm(forms.ModelForm):
	name = forms.CharField(max_length=100)
	email = forms.EmailField(max_length=100)
	phone_number = forms.CharField(max_length=100)
	city = forms.CharField(max_length=100)
	state = forms.CharField(max_length=100)
	zipcode =forms.IntegerField()
	class Meta:
		model = Address
		fields = "__all__"



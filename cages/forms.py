from .models import UserProfile
from django.contrib.auth.models import User
from django import forms
from .models import BbrCustomer, BbrAddress
from django.utils.translation import ugettext_lazy as _

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username', 'email', 'password')

class CustomerForm(forms.ModelForm):
	class Meta:
		model = BbrCustomer
		fields = ('fname', 'lname', 'phone', 'email', 'paymenttype')
		labels = {
			'fname': _("First Name"), 'lname': _("Last Name"), 'paymenttype': _("Payment Type")
		}

class AddressForm(forms.ModelForm):
	class Meta:
		model = BbrAddress
		fields = ('street', 'city', 'state', 'zip')

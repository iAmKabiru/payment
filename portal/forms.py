from django import forms
from django.forms import ModelForm
from .models import Registration, Session


class PaymentForm(forms.ModelForm):

	
	class Meta:
		model = Registration
		fields = ['confirm']
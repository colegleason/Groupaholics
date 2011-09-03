from django import forms

class RegistrationForm(forms.Form):
	email = forms.EmailField()
	password = forms.CharField(max_length=100)
	passwordConfirm = forms.CharField(max_length=100)
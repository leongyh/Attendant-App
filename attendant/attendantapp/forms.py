from django import forms

class RegistrationForm(forms.Form):
	username = forms.CharField(label='Username*', required=True, max_length=100)
	password = forms.CharField(label='Password*', required=True, max_length=100)
	password_repeat = forms.CharField(label='Re-confirm password*', required=True, max_length=100)
	firstName = forms.CharField(label='First Name*', required=True, max_length=100)
	lastName = forms.CharField(label='Last Name*', required=True, max_length=100)
	email = forms.CharField(label='E-mail address*', required=True, max_length=250)
	phone = forms.CharField(label='Phone', max_length=20)
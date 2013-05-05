# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader
from django.contrib.auth.models import User

from attendantapp.forms import *

def login(request):
	template = loader.get_template('attendantapp/login.html'
	
	return HttpResponse(template.render(context))

def register(request):
	if request.method == 'POST': # If the form has been submitted...
		form = RegistrationForm(request.POST) # A form bound to the POST data
		if form.is_valid(): # All validation rules pass
			# Process the data in form.cleaned_data
			# ...
			user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
			user.save()
			
			return HttpResponseRedirect('/index') # Redirect after POST
	else:
		form = RegistrationForm() # An unbound form

	return render(request, 'register.html', {
		'form': form,
	})


	template = loader.get_template('attendantapp/register.html'
	
	return HttpResponse(template.render(context))


def index(request):
	return HttpResponse("Hello, world. You're at the poll index.")

# Actions------------
def register(request):

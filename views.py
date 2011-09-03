from django.shortcuts import render_to_response, HttpResponseRedirect
from django.template import RequestContext
from forms import *

def main(request):
	regForm = RegistrationForm()
	context = RequestContext(request, {'registrationForm': regForm})
	return render_to_response('main.html', context)

def register_script(request):
	context = RequestContext(request, {'foo': 'bar'})
	return HttpResponseRedirect('../registerSuccess.html')
	
def register(request):
	context = {}
	return render_to_response('register.html', context)
	
def register_success(request):
	context = {}
	return render_to_response('registerSuccess.html', context)
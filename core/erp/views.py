from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def myfirstview(request):
	data = {
		'nombre': 'Rafael'

	}
	return render(request, 'index.html', data)
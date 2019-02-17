from django.shortcuts import render
from django.contrib.auth import logout as auth_logout
from django.http import HttpResponse, HttpResponseRedirect
from oauth2client.contrib.django_util.storage import DjangoORMStorage
from .models import *
from django.db.models import Q


def login(request):
	return render(request, 'login.html')

def home(request):
	f = str(request.user)
	if f=="admin":
		data = User.objects.filter(~Q(username=f))
		context= {
		"key":data
		}
		return render(request, 'display.html',context)
	return render(request, 'home.html')



def logout(request):
    """Logs out user"""
    auth_logout(request)
    return HttpResponseRedirect('/')

def delete(request,name):
	User.objects.filter(username=name).delete()  
	return HttpResponseRedirect('/home')

import time
import datetime
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def index(request):
	

	return render(request, 'index.html')

def contact(request):
	

	return render(request, 'contact.html')

def about(request):
	

	return render(request, 'about.html')

def post(request):
	

	return render(request, 'post.html')
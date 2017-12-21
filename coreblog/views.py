
import time
import datetime
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls import url, include
from django.core import serializers
from django.db.models import Q
# Create your views here.


def index(request):
	
	Posts = Post.objects.all().order_by('-id')
	Categories = Category.objects.all()


	return render(request, 'index.html', {'Posts':Posts, 'Categories':Categories})

def contact(request):
	

	return render(request, 'contact.html')

def about(request):
	

	return render(request, 'about.html')

def post(request, slug=None,pk=None):

	P_detail = get_object_or_404(Post, id=pk)
	

	return render(request, 'post.html', {'P_detail':P_detail})

def category(request,slug= None):
	Posts = Post.objects.filter(Category__Name=slug)
	

	return render(request, 'category.html',{'Posts':Posts})
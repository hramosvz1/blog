
import time
import datetime
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls import url, include
from django.core import serializers
from django.db.models import Q
from django.core.paginator import Paginator , EmptyPage, PageNotAnInteger
from django.urls import reverse
# Create your views here.


def index(request):
	
	Posts = Post.objects.all().order_by('-id')
	Categories = Category.objects.all()
	pag = Paginate(request, Posts, 5)



	return render(request, 'index.html', {'Posts':Posts, 'Categories':Categories, 'paginator': pag})

def contact(request):
	

	return render(request, 'contact.html')

def about(request):
	

	return render(request, 'about.html')

def post(request, slug=None,pk=None):

    P_detail = get_object_or_404(Post, id=pk)
    Lasts_posts = Post.objects.all().order_by('-id')
    Categories = Category.objects.all()

    return render(request, 'post.html', {'P_detail':P_detail,'Lasts_posts':Lasts_posts,'Categories':Categories})

def category(request,slug= None):
    Posts = Post.objects.filter(Category__Name=slug).order_by('-id')
    Lasts_posts = Post.objects.all().order_by('-id')
    sCategory = get_object_or_404(Category, Name=slug)
    Categories = Category.objects.all()
    pag = Paginate(request, Posts, 8)

    return render(request, 'category.html',{'Posts':Posts, 'Categories':Categories,'sCategory':sCategory, 'paginator': pag, 'Lasts_posts':Lasts_posts})


def login(request):


    return render(request, 'login.html')


def Paginate(request, queryset, pages):
    """
    PARAMETROS:
    request: Request de la vista
    queryset: Queryset a utilizar en la paginación
    pages: Cantidad de paginas del paginador
    """
    # Retorna el objeto paginator para comenzar el trabajo
    result_list = Paginator(queryset, pages)
 
    try:
        # Tomamos el valor de parametro page, usando GET
        page = int(request.GET.get('page'))
    except:
        page = 1
 
    # Si es menor o igual a 0 igualo en 1
    if page <= 0:
        page = 1
 
    # Si viene un parámetro que es mayor a la cantidad
    # de paginas le igualo el parámetro con las cant de paginas
    if(page > result_list.num_pages):
        page = result_list.num_pages
 
    # Verificamos si esta dentro del rango
    if (result_list.num_pages >= page):
        # Obtengo el listado correspondiente al page
        pagina = result_list.page(page)
 
        context = {
            'queryset': pagina.object_list,
            'page': page,
            'pages': result_list.num_pages,
            'has_next': pagina.has_next(),
            'has_prev': pagina.has_previous(),
            'next_page': page+1,
            'prev_page': page-1,
            'firstPage': 1,
        }
 
    return context
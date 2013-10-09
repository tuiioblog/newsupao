# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from datetime import datetime
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.template.context import RequestContext
from models import *
from forms import *
from django.contrib.auth.decorators import login_required

def home(request):
	categorias = Categoria.objects.all()
	enlaces = Enlace.objects.all()
	template = "index.html"
	#diccionario = {"categorias": categorias, "enlaces": enlaces}
	return render_to_response(template, locals())

def categoria(request, id_categoria):
	categorias = Categoria.objects.all()
	cat = get_object_or_404(Categoria, pk = id_categoria) 
	#cat = Categoria.objects.get(pk = id_categoria)
	enlaces = Enlace.objects.filter(categoria = cat)
	template = "index.html"
	return render_to_response(template, locals()) 

@login_required
def minus(request, id_enlace):
	enlace = Enlace.objects.get(pk=id_enlace)
	enlace.votos = enlace.votos - 1
	enlace.save()
	return HttpResponseRedirect("/")
@login_required
def plus(request, id_enlace):
	enlace = Enlace.objects.get(pk=id_enlace)
	enlace.votos = enlace.votos + 1
	enlace.save()
	return HttpResponseRedirect("/")
@login_required
def add(request):
	categorias = Categoria.objects.all()
	if request.method == "POST":
		form = EnlaceForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/")
	else:
		form = EnlaceForm()

	template = "form.html"
	return render_to_response(template, context_instance = RequestContext(request,locals()))


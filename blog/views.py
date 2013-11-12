# Create your views here.
from django.template.response import TemplateResponse
from django.shortcuts import get_object_or_404
from blog.models import Blog

def home(request):
	return TemplateResponse(request, "home.html", {'blogs': Blog.objects.all()})

def blog(request, slug):
	blog = get_object_or_404(Blog, slug = slug)
	return TemplateResponse(request, "blog.html", {'blog': blog})
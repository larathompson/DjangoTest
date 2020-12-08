from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# this handles traffick from the blog
#return an http response with an h1 tag

def home(request):
  return render(request, 'blog/home.html')

def about(request):
  return HttpResponse('<h1>Blog About </>')


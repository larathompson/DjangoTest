from django.shortcuts import render

posts = [
  {
    'author' : 'Corey',
    'title' : 'Blog Post 1',
    'content' : '1st post',
    'date_posted' : 'Auguts 27, 2018'
  },
   {
    'author' : 'Jane',
    'title' : 'Blog Post 2',
    'content' : '12jd post',
    'date_posted' : 'Auguts 28, 2018'
  },

]


# Create your views here.
# this handles traffick from the blog
#return an http response with an h1 tag

def home(request):
  context = {
    'posts' : posts
  }
  return render(request, 'blog/home.html', context)

def about(request):
  return render(request, 'blog/about.html', {'title': 'About'})


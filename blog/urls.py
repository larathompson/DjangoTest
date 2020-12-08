from django.urls import path
from . import views


#views.home is the function that we have created in the views that does the HTTP method
# now you have ampty string as processed blog part
#then go views.home

urlpatterns = [
    path('', views.home, name="blog-home"),
    path('about/', views.about, name="blog-about"),
]

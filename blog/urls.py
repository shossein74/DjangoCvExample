from blog.views import *
from django.urls import path

urlpatterns = [
    path('blog-home', blog_home, name="blog-home"),
    path('blog-single', blog_single, name="blog-single")
]
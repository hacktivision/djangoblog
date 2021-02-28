from django.shortcuts import render
from django.http import HttpResponse

from .models import Post

def index(request):
    posts = Post.objects.all()
    return HttpResponse([f'<h2>{post.title}</h2><p>{post.text}</p><hr>' for post in posts])
    

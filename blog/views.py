from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.utils import timezone

from .models import Post

def posts_list(request):
    posts = Post.objects.filter(published_date__lt=timezone.now()).order_by('published_date')
    context = {
        'title': 'My posts',
        'posts': posts,
        'count': posts.count()
    }
    return render(request, 'blog/posts.html', context=context)

def post_detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    context = {
        'title': post.title,
        'text': posts.text,
    }
    return render(request, 'blog/post_detail.html', context=context)
    
    

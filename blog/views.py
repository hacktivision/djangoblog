from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.utils import timezone

from .models import Post

def post_list(request):
    posts = Post.objects.filter(published_date__lt=timezone.now()).order_by('published_date')
    context = {
        'title': 'My posts',
        'posts': posts,
        'count': posts.count()
    }
    return render(request, 'blog/posts.html', context=context)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {
        'post': post,
    }
    return render(request, 'blog/post_detail.html', context=context)
    
    

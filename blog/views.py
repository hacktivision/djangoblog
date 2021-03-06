from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.utils import timezone

from .models import Post
from .forms import PostForm

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

    
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    
    form = PostForm()
    context = {
        'title': 'Добовление поста',
        'form': form,
    }
    return render(request, 'blog/post_new.html', context=context)

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    
    form = PostForm(instance=post)
    context = {
        'title': 'Добовление поста',
        'form': form,
    }
    return render(request, 'blog/post_new.html', context=context)
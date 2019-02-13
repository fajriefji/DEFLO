from django.shortcuts import render, redirect
from .models import Blog
from .form import PostForm
from django.utils import timezone

# def Blog(request):
#     return render (request, 'Blog/Blog.html', {})

def db_blog(request):
    blog = Blog.objects.all()
    return render(request, 'Blog/Blog.html', {'blogs' : blog})

def input_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.tanggal = timezone.now()
            post.save()
            return redirect('Blog')
    else:
        form = PostForm()
    return render(request, 'Blog/new_post.html', {'form' : form})
from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog,Category,Tag,Comment
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
# Create your views here.
def blog_list(request):
    blogs = Blog.objects.all().order_by('-date')
    categories = Category.objects.all()
    tags = Tag.objects.all()
    current_user = request.user
    
    if current_user.is_authenticated:
        enrolled_blogs = current_user.blogs_joined.all()
        blogs = Blog.objects.all().order_by('-date')
        for blog in enrolled_blogs:
            blogs = blogs.exclude(id = blog.id)

    else:
        blogs = Blog.objects.all().order_by('-date')
    context = {
        
        'blogs' : blogs,
        'categories':categories,
        'tags':tags
    }
    return render(request,'blogs.html',context)

def blog_detail(request, category_slug, blog_id):
    current_user = request.user
    blog = Blog.objects.get(category__slug=category_slug, id=blog_id)
    blogs = Blog.objects.all().order_by('-date')
    categories = Category.objects.all()
    tags = Tag.objects.all()
    
    if current_user.is_authenticated:
        enrolled_blogs = current_user.blogs_joined.all()
    else:
        enrolled_blogs = Blog.objects.all()
    
    comments = Comment.objects.filter(blog=blog, parent=None).order_by('-created_at')
    
    context = {
        'blog': blog,
        'enrolled_blogs': enrolled_blogs,
        'categories': categories,
        'tags': tags,
        'comments': comments
    }
    return render(request, 'blog.html', context)

def category_list(request,category_slug):
    blogs= Blog.objects.all().filter(category__slug=category_slug)
    categories = Category.objects.all()
    tags = Tag.objects.all()
    context = {
        'blogs':blogs,
         'categories':categories,
         'tags':tags
    }
    return render(request,'blogs.html',context)

def tag_list(request,tag_slug):
    blogs= Blog.objects.all().filter(tags__slug=tag_slug)
    categories = Category.objects.all()
    tags = Tag.objects.all()
    context = {
        'blogs':blogs,
         'categories':categories,
         'tags':tags
    }
    return render(request,'blogs.html',context)

def search(request):
    blogs = Blog.objects.filter(name__contains = request.GET['search'])
    categories = Category.objects.all()
    tags = Tag.objects.all()
    context = {
        'blogs':blogs,
         'categories':categories,
         'tags':tags
    }
    return render(request,'blogs.html',context)

@login_required
def add_comment(request, blog_id):
    if request.method == 'POST':
        blog = get_object_or_404(Blog, id=blog_id)
        content = request.POST.get('content')
        
        if content:
            Comment.objects.create(
                blog=blog,
                user=request.user,
                content=content
            )
            messages.success(request, 'Yorumunuz başarıyla eklendi.')
            return redirect('blog_detail', category_slug=blog.category.slug, blog_id=blog.id)
        else:
            messages.error(request, 'Yorum içeriği boş olamaz.')
            return redirect('blog_detail', category_slug=blog.category.slug, blog_id=blog.id)
    
    return redirect('blog_detail', category_slug=blog.category.slug, blog_id=blog.id)

def get_comments(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    comments = Comment.objects.filter(blog=blog, parent=None)
    
    comments_data = []
    for comment in comments:
        comments_data.append({
            'id': comment.id,
            'user': comment.user.username,
            'content': comment.content
        })
    
    return JsonResponse({'comments': comments_data})
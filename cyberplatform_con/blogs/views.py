from django.shortcuts import render
from .models import Blog,Category,Tag
# Create your views here.
def blog_list(request):
    blogs = Blog.objects.all().order_by('-date')
    categories = Category.objects.all()
    tags = Tag.objects.all()
    context = {
        
        'blogs' : blogs,
        'categories':categories,
        'tags':tags
    }
    return render(request,'blogs.html',context)

def blog_detail(request,category_slug,course_id):
    blog = Blog.objects.get(category__slug=category_slug,id = course_id)
    
    context = {
        'blog':blog
    }
    return render(request,'blog.html',context)

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
from django.shortcuts import render
from .models import Blog,Category,Tag
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

def blog_detail(request,category_slug,blog_id):
    current_user = request.user
    blog = Blog.objects.get(category__slug=category_slug,id = blog_id)
    blogs = Blog.objects.all().order_by('-date')
    categories = Category.objects.all()
    tags = Tag.objects.all()
    
    if current_user.is_authenticated:
        enrolled_blogs = current_user.blogs_joined.all()
    
    else:
        enrolled_blogs =  Blog.objects.all()
    context = {
        'blog':blog,
        'enrolled_blogs' : enrolled_blogs,
        'categories': categories,
        'tags':tags
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
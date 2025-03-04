from django.shortcuts import render
from .models import Blog
# Create your views here.
def blog_list(request):
    blogs = Blog.objects.all().order_by('-date')
    
    context = {
        'blogs' : blogs
    }
    return render(request,'blogs.html',context)

def blog_detail(request,category_slug,course_id):
    blog = Blog.objects.get(category__slug=category_slug,id = course_id)
    
    context = {
        'blog':blog
    }
    return render(request,'blog.html',context)
from django.db import models
from django.contrib.auth.models import User
class Category(models.Model):
    name = models.CharField(max_length=50,null=True)
    slug = models.SlugField(max_length = 50,unique=True,null=True)
    
    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=50,null=True)
    slug = models.SlugField(max_length = 50,unique=True,null=True)
    
    def __str__(self):
        return self.name
    
    
    
class Blog(models.Model):
    name = models.CharField(max_length=200,unique=True)
    category = models.ForeignKey(Category,null=True,on_delete=models.DO_NOTHING)
    tags = models.ManyToManyField(Tag,blank=True,null=True)
    image = models.ImageField(upload_to="blogs/%Y/%m/%d/",default="blogs/default.jpg")
    customer = models.ManyToManyField(User,blank=True,related_name='blogs_joined')
    description = models.TextField(blank=True,null=True)
    blog_url = models.CharField(max_length=200,null=True)
    date = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    


from django.urls import path
from . import views

urlpatterns = [
   path('',views.blog_list,name="blogs"),
   path('<slug:category_slug>/<int:course_id>',views.blog_detail,name='blog_detail'),
    
]

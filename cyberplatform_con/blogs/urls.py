from django.urls import path
from . import views

urlpatterns = [
   path('',views.blog_list,name="blogs"),
   path('<slug:category_slug>/<int:blog_id>',views.blog_detail,name='blog_detail'),
   path('categories/<slug:category_slug>',views.category_list,name="blogs_by_category"),
   path('tags/<slug:tag_slug>',views.tag_list,name="blogs_by_tag"),
   path('search/',views.search,name="search"),
]

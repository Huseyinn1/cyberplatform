from django.contrib import admin
from .models import Blog,Category,Tag,Comment



@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
        list_display = ('name','available')
        list_filter = ('available',)
        search_fields = ('name','description')
        
@admin.register(Category)
class Category(admin.ModelAdmin):
        prepopulated_fields = {'slug':('name',)}
        
@admin.register(Tag)
class Category(admin.ModelAdmin):
        prepopulated_fields = {'slug':('name',)}

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
        list_display = ('user','blog','content','created_at')
        list_filter = ('created_at','user','blog')
        search_fields = ('content','user__username','blog__name')
        date_hierarchy = 'created_at'
        ordering = ('-created_at',)
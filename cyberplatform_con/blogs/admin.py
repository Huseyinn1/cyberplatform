from django.contrib import admin
from .models import Blog,Category,Tag



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
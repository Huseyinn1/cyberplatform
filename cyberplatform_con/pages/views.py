from django.shortcuts import render
from django.views.generic import TemplateView
from blogs.models import Blog

# Create your views here.
#def index(request):
 #   return render(request,'index.html')
class IndexView(TemplateView):
    template_name = 'index.html'
     
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blogs'] = Blog.objects.filter(available=True).order_by('date')[:2]
        context['total_blogs'] = Blog.objects.filter(available=True).count()
        return context
class AboutView(TemplateView):
    template_name = 'about.html' 
#def about(request):
  #  return render(request,'about.html')


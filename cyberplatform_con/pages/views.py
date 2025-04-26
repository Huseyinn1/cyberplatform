from django.shortcuts import render
from django.views.generic import TemplateView
from blogs.models import Blog


# views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage

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
def ocr_view(request):
    return render(request, 'ocr.html')

@csrf_exempt  # CSRF korumasını geçici olarak devre dışı bırakıyoruz (gerçek uygulamalarda CSRF'yi uygun şekilde yapılandırmalısınız)
def analyze_image(request):
    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']
        # Burada, dosya üzerinde işlemler yapabilirsiniz
        file_name = default_storage.save(image.name, image)
        return JsonResponse({'message': 'Dosya başarıyla alındı', 'file_name': file_name}, status=200)
    return JsonResponse({'error': 'Geçersiz istek'}, status=400)
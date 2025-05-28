from django.shortcuts import render
from django.views.generic import TemplateView
from blogs.models import Blog
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages


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

def qrcheck_view(request):
    return render(request, 'qr_check.html')

def logparser_view(request):
    return render(request, 'log_parser.html')
def onlinenmap_view(request):
    return render(request, 'online_nmap.html')
def usom_view(request):
    return render(request, 'usom.html')

def ioc_checker_view(request):
    return render(request, 'ioc_checker.html')


def contact_view(request):
    return render(request, 'contact.html')

def contact_message(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        subject = f"Hyperspace Contact Form"
        message_body = f"Message from {name}-{email}: \n\n {message}"
        recipient_list = [settings.EMAIL_HOST_USER]
        
        try:
            send_mail(subject,message_body,email,recipient_list)
        except Exception:
            messages.error(request,"Something happend")
        else:
            messages.success(request,"We have received your email")
    
    return HttpResponseRedirect(reverse('index')+'#three')


@csrf_exempt  # CSRF korumasını geçici olarak devre dışı bırakıyoruz (gerçek uygulamalarda CSRF'yi uygun şekilde yapılandırmalısınız)
def analyze_image(request):
    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']
        # Burada, dosya üzerinde işlemler yapabilirsiniz
        file_name = default_storage.save(image.name, image)
        return JsonResponse({'message': 'Dosya başarıyla alındı', 'file_name': file_name}, status=200)
    return JsonResponse({'error': 'Geçersiz istek'}, status=400)
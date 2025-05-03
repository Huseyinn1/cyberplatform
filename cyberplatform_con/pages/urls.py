from django.urls import path
from . import views
from pages.views import AboutView,IndexView,analyze_image

urlpatterns = [
   path('',IndexView.as_view(),name="index"),
   path('about/',AboutView.as_view(),name="about"),
   path('ocr/', views.ocr_view, name='ocr'),
   path('contact/', views.contact_view, name='contact'),
   path('contact_message',views.contact_message,name="contact_message")

    
]

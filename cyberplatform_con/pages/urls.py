from django.urls import path
from . import views
from pages.views import AboutView,IndexView,analyze_image

urlpatterns = [
   path('',IndexView.as_view(),name="index"),
   path('about/',AboutView.as_view(),name="about"),
   path('ocr/', views.ocr_view, name='ocr'),
   path('contact/', views.contact_view, name='contact'),
   path('contact_message',views.contact_message,name="contact_message"),
   path('qr_check/',views.qrcheck_view,name="qr_check"),
   path('log_parser/',views.logparser_view,name="log_parser"),
   path('online_nmap/',views.onlinenmap_view,name="online_nmap"),
   path('usom/',views.usom_view,name="usom"),
   path('ioc_checker/',views.ioc_checker_view,name="ioc_checker")
]

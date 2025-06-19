from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.user_register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.user_dashboard, name='dashboard'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('enroll_the_blog/', views.enroll_the_blog, name="enroll_the_blog"),
    path('release_the_blog/', views.release_the_blog, name="release_the_blog"),
    path('change-password/', views.change_password, name="change_password"),
]
from django.shortcuts import render, redirect
from . forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from blogs.models import Blog
from django.contrib.auth.models import User
from .models import Profile



def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username,
                                        password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')

                else:
                    messages.info(request, 'Disabled Account')

            else:
                messages.info(request, 'Check Your Username and Password')

    else:
        form = LoginForm()

    return render(request, 'login.html', {'form':form})




def user_register(request):
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account has been created, You can LOGIN')
            return redirect('login')
    
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form':form})

def user_logout(request):
    logout(request)
    return redirect('index')

@login_required(login_url='login')
def user_dashboard(request):
    current_user = request.user

    blogs = current_user.blogs_joined.all()

    context = {
        'blogs': blogs
    }

    return render(request, 'dashboard.html', context)

def enroll_the_blog(request):
    blog_id = request.POST['blog_id']
    user_id = request.POST['user_id']
    blog = Blog.objects.get(id = blog_id)
    user = User.objects.get(id = user_id)
    blog.customer.add(user)
    return redirect('dashboard')



def release_the_blog(request):
    blog = Blog.objects.get(id = request.POST['blog_id'])
    user = User.objects.get(id = request.POST['user_id'])
    blog.customer.remove(user)
    return redirect('dashboard')

@login_required
def edit_profile(request):
    if request.method == 'POST':
        # Kullanıcı bilgilerini güncelle
        user = request.user
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.save()

        # Profil bilgilerini güncelle
        profile = user.profile
        if 'avatar' in request.FILES:
            profile.avatar = request.FILES['avatar']
        profile.bio = request.POST.get('bio')
        profile.phone = request.POST.get('phone')
        profile.address = request.POST.get('address')
        profile.save()

        messages.success(request, 'Profiliniz başarıyla güncellendi.')
        return redirect('dashboard')
    
    return render(request, 'edit_profile.html')

@login_required
def change_password(request):
    if request.method == 'POST':
        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        user = request.user

        if not user.check_password(current_password):
            messages.error(request, '❌ Mevcut şifreniz yanlış! Lütfen tekrar deneyin.')
            return redirect('edit_profile')

        if new_password != confirm_password:
            messages.error(request, '❌ Yeni şifreler eşleşmiyor! Lütfen aynı şifreyi iki kez yazın.')
            return redirect('edit_profile')

        if len(new_password) < 8:
            messages.error(request, '❌ Yeni şifre en az 8 karakter olmalıdır!')
            return redirect('edit_profile')

        user.set_password(new_password)
        user.save()
        
        messages.success(request, '✅ Şifreniz başarıyla değiştirildi! Güvenlik için tekrar giriş yapmanız gerekiyor.')
        logout(request)  # Kullanıcıyı çıkış yaptır
        return redirect('login')

    return redirect('edit_profile')

    
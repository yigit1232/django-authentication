from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm,LoginForm,ResetPasswordForm,ForgotPasswordForm
from django.core.mail import send_mail
from .models import User,ForgotPassword
from config import settings
import secrets
import django
import re

def index(request):
    version = django.get_version()
    return render(request,'index.html',{'version':version})

def signup(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        form = RegisterForm(request.POST or None)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            repassword = form.cleaned_data.get('repassword')
            if name == '' or username == '' or email == '' or password == '' or repassword == '':
                error = 'Please fill all fields'
                return render(request,'register.html',{'form':form,'error':error})
            elif User.objects.filter(username=username).exists():
                error = 'Username already exists'
                return render(request,'register.html',{'form':form,'error':error})
            elif User.objects.filter(email=email).exists():
                error = 'Email already exists'
                return render(request,'register.html',{'form':form,'error':error})
            email_check = re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email)
            if not email_check:
                error = 'Invalid email'
                return render(request,'register.html',{'form':form,'error':error})
            elif password != repassword:
                error = 'Passwords do not match'
                return render(request,'register.html',{'form':form,'error':error})
            elif len(password) < 6:
                error = 'Password must be at least 6 characters'
                return render(request,'register.html',{'form':form,'error':error})
            user = User(username=username,email=email,name=name)
            user.set_password(password)
            user.save()
            return redirect('login')
        else:
            return render(request,'register.html',{'form':form})
    else:
        return render(request,'register.html',{'form':RegisterForm()})
    return render(request,'register.html',{'form':form})

def login_user(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('index')
            else:
                error = 'Invalid username or password'
                return render(request,'login.html',{'form':form,'error':error})
        else:
            return render(request,'login.html',{'form':form})
    else:
            return render(request,'login.html',{'form':LoginForm()})
    return render(request,'login.html',{'form':form})

def forgot_password(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        form = ForgotPasswordForm(request.POST or None)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            user = User.objects.filter(email=email).first()
            if not user:
                error = 'Email not found'
                return render(request,'forgot_password.html',{'form':form,'error':error})
            token = secrets.token_urlsafe(16)
            if ForgotPassword.objects.filter(user_id=user).exists():
                ForgotPassword.objects.filter(user_id=user).delete()
            forgot_password = ForgotPassword(user_id=user,token=token)
            forgot_password.save()
            send_mail(
                'Reset Password',
                f'Please click on the link to reset your password: http://127.0.0.1:8000/password/reset/{token}',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[email],
            )
            success = 'Email sent successfully'
            return render(request,'forgot_password.html',{'form':form,'success':success})
        else:
            return render(request,'forgot_password.html',{'form':form})
    else:
        return render(request,'forgot_password.html',{'form':ForgotPasswordForm()})
    return render(request,'forgot_password.html',{'form':ForgotPasswordForm()})

def reset_password(request,token):
    if not ForgotPassword.objects.filter(token=token).exists():
        return redirect('index')
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        form = ResetPasswordForm(request.POST or None)
        if form.is_valid():
            password = form.cleaned_data.get('password')
            repassword = form.cleaned_data.get('repassword')
            if password != repassword:
                error = 'Passwords do not match'
                return render(request,'reset_password.html',{'form':form,'error':error,'token':token})
            elif len(password) < 6:
                error = 'Password must be at least 6 characters'
                return render(request,'reset_password.html',{'form':form,'error':error,'token':token})
            forgot_password = ForgotPassword.objects.get(token=token)
            user = User.objects.get(id=forgot_password.user_id.id)
            forgot_password.delete()
            if not user:
                error = 'User not found'
                return render(request,'reset_password.html',{'form':form,'error':error,'token':token})
            user.set_password(password)
            user.save()
            return redirect('login')
        else:
            return render(request,'reset_password.html',{'form':form,'token':token})
    else:
        return render(request,'reset_password.html',{'form':ResetPasswordForm(),'token':token})
    return render(request,'reset_password.html',{'form':ResetPasswordForm(),'token':token})

def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('index')
    else:
        return redirect('index')
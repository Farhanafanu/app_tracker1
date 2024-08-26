from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.db import models 
from .forms import SignUpForm, EmailAuthenticationForm
from admin_panel.models import App, Task
from django.db.models import Count,Sum

@login_required
def home(request):
    apps = App.objects.all()
    downloaded_apps_count = Task.objects.filter(user=request.user).count()
    return render(request, 'user/userhome.html', {
        'apps': apps,
        'downloaded_apps_count': downloaded_apps_count
    })

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            auth_login(request, user)
            return redirect('userhome')
    else:
        form = SignUpForm()
    return render(request, 'user/signup.html', {'form': form})

@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        form = EmailAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('userhome')
            else:
                messages.error(request, 'Invalid email or password.')
        else:
            messages.error(request, 'Invalid email or password.')
    else:
        form = EmailAuthenticationForm()
    return render(request, 'user/login.html', {'form': form})

@login_required
def profile(request):
    completed_tasks_count = Task.objects.filter(user=request.user).count()
    total_points = Task.objects.filter(user=request.user).aggregate(total=Sum('points_earned'))['total'] or 0

    context = {
        'completed_tasks_count': completed_tasks_count,
        'total_points': total_points,
    }

    return render(request, 'user/profile.html', context)
def task_page(request, app_id):
    app_instance = App.objects.get(id=app_id)
    
    if request.method == 'POST' and request.FILES.get('screenshot'):
        screenshot = request.FILES['screenshot']
        task = Task.objects.create(
            user=request.user,
            app=app_instance,
            screenshot=screenshot,
            points_earned=app_instance.points
        )
        return redirect('points')
    
    return render(request, 'user/task_page.html', {'app': app_instance})

def points_view(request):
    total_points = Task.objects.filter(user=request.user).aggregate(total=models.Sum('points_earned'))['total'] or 0
    completed_tasks = Task.objects.filter(user=request.user)
    
    return render(request, 'user/points.html', {
        'total_points': total_points,
        'completed_tasks': completed_tasks
    })
@login_required
def tasks_overview(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'user/tasks_overview.html', {
        'tasks': tasks
    })
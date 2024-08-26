from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import AppForm

def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('add-app') 
    else:
        form = AuthenticationForm()
    return render(request, 'admin_panel/custom_login.html', {'form': form})
def admin_home(request):
    return render(request, 'admin_panel/home.html')
def add_app(request):
    if request.method == 'POST':
        form = AppForm(request.POST, request.FILES)
        if form.is_valid():
            print(request.FILES)  
            app_instance = form.save()
            print(f"Uploaded image path: {app_instance.image.path}")
            print(f"Database image field value: {app_instance.image.name}")
            return redirect('admin-home')
        else:
            print("Form is not valid")
            print(form.errors)
    else:
        form = AppForm()
    return render(request, 'admin_panel/add_app.html', {'form': form})

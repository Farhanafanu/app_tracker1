# urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import EmailAuthenticationForm  
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/',views.user_login,name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('userhome', views.home, name='userhome'), 
    path('task/<int:app_id>/', views.task_page, name='task-page'), 
    path('points/', views.points_view, name='points'),
    path('tasks-overview/', views.tasks_overview, name='tasks-overview'),
]

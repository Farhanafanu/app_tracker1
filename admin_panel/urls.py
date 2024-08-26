from django.urls import path
from .views import add_app,custom_login,admin_home

urlpatterns = [

    
    path('custom-login/', custom_login, name='custom_login'),
    path('admin-home/', admin_home, name='admin-home'),
    path('add-app/', add_app, name='add-app'),
]

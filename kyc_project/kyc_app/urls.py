from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
 
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('dashboard/', views.admin_dashboard, name='dashboard'),
    path('user-call/', views.user_call, name='user_call'),
    path('upload-screenshot/', views.upload_screenshot, name='upload_screenshot'),
]
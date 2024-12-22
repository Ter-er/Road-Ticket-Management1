from django.conf import settings
from django.conf.urls.static import static

#from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
#from .forms import MotoristLoginForm

urlpatterns = [
    path('', views.home, name='home'),
    path('admin_login/', views.admin_login_redirect, name='admin_login_redirect'),
    path('motorist_signup/', views.motorist_signup, name='motorist_signup'),
    path('login_user/', views.login_user, name='login_user'),
    path('official_login/', views.official_login, name='official_login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout', views.logout, name='logout'),
    #path('accounts/motorist_login/', auth_views.LoginView.as_view(), name='motorist_login'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
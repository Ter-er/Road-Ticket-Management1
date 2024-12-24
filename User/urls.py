from django.conf import settings
from django.conf.urls.static import static

#from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
#from .forms import MotoristLoginForm

urlpatterns = [
    path('', views.home, name='home'),
    path('admin_site/', views.admin_login_redirect, name='admin_login_redirect'),
    path('motorist_signup/', views.motorist_signup, name='motorist_signup'),
    # path('login_user/', views.login_user, name='login_user'),
    path('official_login/', views.official_login, name='official_login'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('dashboard_official/', views.dashboard_official, name='dashboard_official'),
    path('dashboard_admin/', views.dashboard_admin, name='dashboard_admin'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout_user', views.logout_user, name='logout_user'),
    #path('accounts/motorist_login/', auth_views.LoginView.as_view(), name='motorist_login'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
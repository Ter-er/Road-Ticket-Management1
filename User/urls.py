from django.conf import settings
from django.conf.urls.static import static

#from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
#from .forms import MotoristLoginForm

urlpatterns = [
    path('', views.home, name='home'),
    path('motorist_signup/', views.motorist_signup, name='motorist_signup'),
    path('motorist-login/', views.motorist_login, name='motorist-login'),
    path('official-login/', views.official_login, name='official-login'),
    path('admin-login/', views.admin_login, name='admin-login'),
    path('dashboard-motorist/', views.dashboard_motorist, name='dashboard-motorist'),
    path('dashboard-official/', views.dashboard_official, name='dashboard-official'),
    path('dashboard-admin/', views.dashboard_admin, name='dashboard-admin'),
    path('logout_user', views.logout_user, name='logout_user'),
    path('admin_site/', views.admin_login_redirect, name='admin_login_redirect'),    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
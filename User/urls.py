from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin_login/', views.admin_login_redirect, name='admin_login_redirect'),
    path('motorist_signup/', views.motorist_signup, name='motorist_signup'),
    path('motorist_login/', views.motorist_login, name='motorist_login'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
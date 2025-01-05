from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('create-ticket', views.create_ticket, name='create-ticket'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
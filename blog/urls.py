from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import post_list, post_detail

urlpatterns = [
    path('', post_list, name='post_list'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
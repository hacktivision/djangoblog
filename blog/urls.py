from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import posts_list, post_detail

urlpatterns = [
    path('', posts_list, name='posts_list'),
    path('<int:post_id>', post_detail, name='post_detail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
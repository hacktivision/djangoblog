from django.urls import path

from .views import posts_list, post_detail

urlpatterns = [
    path('', posts_list, name='posts_list'),
    path('<int:post_id>', post_detail, name='post_detail'),
]
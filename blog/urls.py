from django.urls import re_path, path
from . import views

urlpatterns = [
    re_path(r'^$', views.post_list, name='post'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]

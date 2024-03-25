from django.urls import path
from .views import create_content_day, delete_content_day

urlpatterns = [
    path('create_content/', create_content_day, name="create_content"),
    path('delete_content/', delete_content_day, name="delete_content"),
]

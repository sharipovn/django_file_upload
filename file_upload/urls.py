# file_upload/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_file, name='upload_file'),
    path('uploaded/', views.uploaded_files, name='uploaded_files'),
    path('all_uploaded/', views.all_uploaded_files, name='all_uploaded_files'),
    path('delete_file/<int:file_id>/', views.delete_file, name='delete_file'),
    path('delete_file_from_all/<int:file_id>/', views.delete_file_from_all, name='delete_file_from_all'),
]

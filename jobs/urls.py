from . import views
from django.urls import path

urlpatterns = [
    path('', views.JobList.as_view(), name='home'),
    path('post/', views.post_job, name='post_job'),
    path('<slug:slug>/edit/', views.edit_job, name='edit_job'),
    path('<slug:slug>/', views.job_detail, name='job_detail'),
]
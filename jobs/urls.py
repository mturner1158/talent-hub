from . import views
from django.urls import path

urlpatterns = [
    path('', views.JobList.as_view(), name='home'), # url on load showing all job options
    path('post/', views.post_job, name='post_job'), # url to post a job
    path('<slug:slug>/edit/', views.edit_job, name='edit_job'), # url to a specific job to edit
    path('<slug:slug>/', views.job_detail, name='job_detail'), # url to a specific posted job
]
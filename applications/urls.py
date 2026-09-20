from . import views
from django.urls import path

urlpatterns = [
    path('apply/<slug:slug>/', views.apply_to_job, name='apply_to_job'), # url to apply for a job
    path('my-applications/', views.my_applications, name='my_applications'), # url to view submitted applicaitons
]
from . import views
from django.urls import path

urlpatterns = [
    path('', views.JobList.as_view(), name='home'),
]
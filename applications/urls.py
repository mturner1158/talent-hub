from . import views
from django.urls import path

urlpatterns = [
    path('apply/<slug:slug>/', views.apply_to_job, name='apply_to_job'),
    # path('applications/', views.index, name='applicants'),
]
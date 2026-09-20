from . import views
from django.urls import path

urlpatterns = [
    path('dashboard/', views.dashboard, name='company_dashboard'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
]
from . import views
from django.urls import path

urlpatterns = [
    # url to company dashbaord page
    path('dashboard/', views.dashboard, name='company_dashboard'),
    # url to company profile edit form
    path('profile/edit/', views.edit_profile, name='edit_profile'),
]

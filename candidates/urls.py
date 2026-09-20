from . import views
from django.urls import path

urlpatterns = [
    path('profile/edit/', views.edit_profile, name='edit_candidate_profile'),
]
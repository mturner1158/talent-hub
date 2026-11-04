from . import views
from django.urls import path


urlpatterns = [
    # url to edit candidate profile
    path('profile/edit/',
         views.edit_profile,
         name='edit_candidate_profile'),
]

from . import views
from django.urls import path

urlpatterns = [
    # url to apply for a job
    path('apply/<slug:slug>/',
         views.apply_to_job,
         name='apply_to_job'),
    # url to view applications to a role
    path('review/<slug:job_slug>/',
         views.review_applications,
         name='review_applications'),
    # url to view submitted applications
    path('my-applications/',
         views.my_applications,
         name='my_applications'),
    # update application status when reviewing an application
    path('status/<int:pk>/',
         views.update_status,
         name='update_status'),
    # url for a user to withdraw an application
    path('withdraw/<int:pk>/',
         views.withdraw_application,
         name='withdraw_application'),
]

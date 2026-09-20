from . import views
from django.urls import path

urlpatterns = [
    path('apply/<slug:slug>/', views.apply_to_job, name='apply_to_job'), # url to apply for a job
    path('review/<slug:job_slug>/', views.review_applications, name='review_applications'), # url to view applications to a role
    path('my-applications/', views.my_applications, name='my_applications'), # url to view submitted applicaitons
    path('status/<int:pk>/', views.update_status, name='update_status'), # update application status when reviewing an applicaiton
    path('withdraw/<int:pk>/', views.withdraw_application, name='withdraw_application'), # url for a user to withdraw an application
]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path('summernote/', include('django_summernote.urls')),
    path('', include('jobs.urls'), name='jobs-urls'),
    path('applications/', include('applications.urls'),
         name='applications-urls'),
    path('companies/', include('companies.urls'), name='companies-urls'),
    path('candidates/', include('candidates.urls'), name='candidates-urls')
]

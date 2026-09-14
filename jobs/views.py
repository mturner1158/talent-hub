from django.shortcuts import render 
from django.views import generic
from .models import Job

# Create your views here. 
class JobList(generic.ListView):
    queryset = Job.objects.all()
    template_name = "job_list.html"
    paginate_by = 4


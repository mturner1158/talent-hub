from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Job

# Create your views here. 
class JobList(generic.ListView):
    queryset = Job.objects.all()
    template_name = "job_list.html"
    # paginate_by = 4

def job_detail(request, slug):
    """
    Shows an instance of the job moddel and displays in the job_detail.html template
    """
    queryset = Job.objects.filter(is_active=1)
    job = get_object_or_404(queryset, slug=slug)
    return render(
        request,
        "jobs/job_detail.html",
        {"job": job},
    )

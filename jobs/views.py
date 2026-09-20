from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Job
from .forms import JobForm, JobEditForm
from applications.forms import ApplicationForm

# Create your views here. 
class JobList(generic.ListView):
    queryset = Job.objects.all()
    template_name = "job_list.html"
    # paginate_by = 4

def job_detail(request, slug):
    """
    Shows an instance of the job model and displays in the job_detail.html template
    """
    queryset = Job.objects.filter(is_active=1)
    job = get_object_or_404(queryset, slug=slug)
    form = ApplicationForm() # link my application form to job_detail for the modal
    return render(
        request,
        "jobs/job_detail.html",
        {"job": job,
         "form": form},
    )

@login_required
def post_job(request):
    """
    Provides access to the form required to post a job
    """
    if not hasattr(request.user, 'company_contact'):  # match your actual related_name
        raise PermissionDenied("Only companies can post a job.")

    company = request.user.company_contact
    form = JobForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        job = form.save(commit=False)
        job.company = company
        job.save()
        return redirect('job_detail', slug=job.slug)

    return render(
        request, 
        'jobs/job_form.html', 
        {'form': form}
    )

@login_required
def edit_job(request, slug):
    job = get_object_or_404(Job, slug=slug)

    if job.company != request.user.company_contact:
        raise PermissionDenied("You can only edit your own job listings.")

    form = JobEditForm(request.POST or None, instance=job)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('job_detail', slug=job.slug)

    return render(request, 'jobs/job_edit.html', {'form': form, 'job': job})
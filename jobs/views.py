from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib import messages
from .models import Job
from .forms import JobForm, JobEditForm
from applications.forms import ApplicationForm

# Create your views here. 
class JobList(generic.ListView):
    template_name = "job_list.html"
    context_object_name = "job_list"

    def get_queryset(self):
        queryset = Job.objects.filter(is_active=True)

        keyword = self.request.GET.get('keyword')
        location = self.request.GET.get('location')
        job_type = self.request.GET.get('job_type')

        if keyword:
            queryset = queryset.filter(title__icontains=keyword)
        if location:
            queryset = queryset.filter(location__icontains=location)
        if job_type:
            queryset = queryset.filter(job_type=job_type)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['keyword'] = self.request.GET.get('keyword', '')
        context['location'] = self.request.GET.get('location', '')
        context['job_type'] = self.request.GET.get('job_type', '')
        context['job_type_choices'] = Job._meta.get_field('job_type').choices
        return context

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
        messages.success(request, "Job posted successfully!")
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
        messages.success(request, "Job updated successfully!")
        return redirect('job_detail', slug=job.slug)

    return render(
        request, 
        'jobs/job_edit.html', 
        {'form': form, 
         'job': job}
    )
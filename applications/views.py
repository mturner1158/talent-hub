from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from jobs.models import Job
from .models import Application
from .forms import ApplicationForm

# only logged in users can see this view
@login_required
def apply_to_job(request, slug):
    # confirm the user is a candidate
    if not hasattr(request.user, 'candidate_profile'): 
        raise PermissionDenied("Only candidates can apply.")

    job = get_object_or_404(Job, slug=slug, is_active=True)
    candidate = request.user.candidate_profile

    # check to see if a user has already submitted an applicaiton
    if Application.objects.filter(job=job, candidate=candidate).exists():
        messages.warning(request, "You've already applied to this job.")
        return redirect('job_detail', slug=job.slug)

    # application submission
    form = ApplicationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        application = form.save(commit=False)
        application.job = job
        application.candidate = candidate
        application.save()
        messages.success(request, "Application submitted!")
        return redirect('my_applications')

    return render(
        request, 
        'applications/apply.html',
        {'form': form, 'job': job}
        )
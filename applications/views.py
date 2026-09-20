from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from jobs.models import Job
from .models import Application
from .forms import ApplicationForm

# only logged in users can see this view
@login_required
# view to apply for a job
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

# only logged in users can see this view
@login_required
# view for all applications a user has submitted
def my_applications(request):
    # confirm the user is a candidate
    if not hasattr(request.user, 'candidate_profile'):
        raise PermissionDenied("Only candidates have an applications list.")
    applications = Application.objects.filter(candidate=request.user.candidate_profile)
    return render(request, 'applications/my_applications.html', {'applications': applications})


# only logged in users can see this view
@login_required
# view for a user to withdraw an application
def withdraw_application(request, pk):
    application = get_object_or_404(Application, pk=pk)

    if not hasattr(request.user, 'candidate_profile') or application.candidate != request.user.candidate_profile:
        raise PermissionDenied("You can only withdraw your own applications.")

    if request.method == 'POST':
        application.delete()
        messages.success(request, "Application withdrawn.")

    return redirect('my_applications')


# only logged in users can see this view
@login_required
# view for companies to see what applications are submitted to their roles
def review_applications(request, job_slug):
    job = get_object_or_404(Job, slug=job_slug)
    # confirm user is a company and jobs are owned by that company
    if not hasattr(request.user, 'company_contact') or job.company != request.user.company_contact:
        raise PermissionDenied("You can only view applicants for your own jobs.")

    applications = job.applications.all()
    return render(
        request, 
        'applications/review_applications.html', 
        {'job': job, 
         'applications': applications,
         'status_choices': Application._meta.get_field('status').choices}
        )

# only logged in users can see this view
@login_required
# view for companies to update the status of an application
def update_status(request, pk):
    application = get_object_or_404(Application, pk=pk)
    # confirm user is a company and jobs are owned by that company
    if not hasattr(request.user, 'company_contact') or application.job.company != request.user.company_contact:
        raise PermissionDenied

    if request.method == 'POST':
        new_status = request.POST.get('status')
        if new_status in dict(Application.STATUS_CHOICES):
            application.status = new_status
            application.save()
            messages.success(request, "Status updated.")

    return redirect('review_applications', job_slug=application.job.slug)
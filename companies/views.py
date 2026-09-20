from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404, redirect
from jobs.models import Job
from applications.models import Application


# requires user to be logged in
@login_required
def dashboard(request):
    if not hasattr(request.user, 'company_contact'):
        raise PermissionDenied

    company = request.user.company_contact
    jobs = company.jobs.all()  # confirm this related_name matches your Job.company field
    active_jobs_count = jobs.filter(is_active=True).count()
    unique_applicants_count = Application.objects.filter(job__company=company).values('candidate').distinct().count()

    return render(request, 'companies/dashboard.html', {
        'jobs': jobs,
        'active_jobs_count': active_jobs_count,
        'unique_applicants_count': unique_applicants_count,
    })
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from jobs.models import Job
from applications.models import Application
from .forms import CompanyProfileForm

# requires user to be logged in
@login_required
def dashboard(request):
    # only companies can use this view
    if not hasattr(request.user, 'company_contact'):
        raise PermissionDenied

    company = request.user.company_contact
    jobs = company.jobs.all()  # confirm this related_name matches your Job.company field
    active_jobs_count = jobs.filter(is_active=True).count()
    unique_applicants_count = Application.objects.filter(job__company=company).values('candidate').distinct().count()

    return render(
        request, 
        'companies/dashboard.html', 
        {'jobs': jobs,
        'active_jobs_count': active_jobs_count,
        'unique_applicants_count': unique_applicants_count,
        }
    )

# requries user to be logged on
@login_required
# allows a company to edit its profile 
def edit_profile(request):
    if not hasattr(request.user, 'company_contact'):
        raise PermissionDenied("Only companies have a profile to edit.")

    company = request.user.company_contact
    form = CompanyProfileForm(request.POST or None, instance=company)

    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "Profile updated.")
        return redirect('company_dashboard')

    return render(
        request, 
        'companies/edit_profile.html', 
        {'form': form}
        )
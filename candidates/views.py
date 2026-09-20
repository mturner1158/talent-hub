from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CandidateProfileForm

# requires user to be logged in
@login_required
# allows a user to edit their profile with new details
def edit_profile(request):
    # check the user is a candiadate
    if not hasattr(request.user, 'candidate_profile'):
        raise PermissionDenied("Only candidates have a profile to edit.")

    candidate = request.user.candidate_profile
    form = CandidateProfileForm(request.POST or None, instance=candidate)

    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "Profile updated.")
        return redirect('my_applications')

    return render(
        request, 
        'candidates/edit_profile.html', 
        {'form': form}
        )
from django import forms

from companies.models import Companies
from candidates.models import Candidate


class RoleSignupForm(forms.Form):
    ROLE_CHOICES = (
        ('company', 'Company'),
        ('candidate', 'Candidate'),
    )

    role = forms.ChoiceField(
        choices=ROLE_CHOICES,
        widget=forms.RadioSelect,
        label="I am signing up as a..."
    )

    def signup(self, request, user):
        role = self.cleaned_data['role']

        if role == 'company':
            Companies.objects.create(
                owner=user,
                company_name=user.username,
                description='',
                sectors=''
            )
        else:
            Candidate.objects.create(
                account=user,
                first_name=user.username,
                last_name='',
                personal_statment='',
                skills='',
                experience=''
            )
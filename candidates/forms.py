from django import forms
from django_summernote.widgets import SummernoteWidget
from talenthub.sanitise import clean_html
from .models import Candidate


# form to edit candidate profile
class CandidateProfileForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = [
            'first_name',
            'last_name',
            'personal_statement',
            'skills',
            'experience',
        ]
        widgets = {
            'skills': SummernoteWidget(),
            'experience': SummernoteWidget(),
        }

    def clean_skills(self):
        return clean_html(self.cleaned_data['skills'])

    def clean_experience(self):
        return clean_html(self.cleaned_data['experience'])

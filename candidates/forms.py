from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Candidate

class CandidateProfileForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = ['first_name', 'last_name', 'personal_statement', 'skills', 'experience']
        widgets = {
            'personal_statement': SummernoteWidget(),
            'skills': SummernoteWidget(),
            'experience': SummernoteWidget(),
        }
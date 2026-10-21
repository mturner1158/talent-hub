from django import forms
from django_summernote.widgets import SummernoteWidget
from talenthub.sanitise import clean_html
from .models import Job

# post a job form

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description', 'location', 'salary_min', 'salary_max', 'job_type']
        widgets = {
            'description': SummernoteWidget(),
        }

    def clean_description(self):
        return clean_html(self.cleaned_data['description'])

# edit a job form

class JobEditForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description', 'location', 'salary_min', 'salary_max', 'job_type', 'is_active']
        widgets = {
            'description': SummernoteWidget(),
        }

    def clean_description(self):
        return clean_html(self.cleaned_data['description'])
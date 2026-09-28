from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Job

# post a job form

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description', 'location', 'salary_min', 'salary_max', 'job_type']
        widgets = {
            'description': SummernoteWidget(),
        }

# edit a job form

class JobEditForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description', 'location', 'salary_min', 'salary_max', 'job_type', 'is_active']
        widgets = {
            'description': SummernoteWidget(),
        }
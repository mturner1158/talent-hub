from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Job

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description', 'location', 'salary_min', 'salary_max', 'job_type']
        widgets = {
            'description': SummernoteWidget(),
        }
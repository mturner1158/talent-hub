from django import forms
from .models import Application

class ApplicationForm(forms.ModelForm):
    # form used to apply for a role
    class Meta:
        model = Application
        fields = ['cover_note', 'uk_working_status']
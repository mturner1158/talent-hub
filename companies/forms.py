from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Companies

class CompanyProfileForm(forms.ModelForm):
    class Meta:
        model = Companies
        fields = ['company_name', 'description', 'website', 'sectors']
        widgets = {
            'description': SummernoteWidget(),
            'sectors': SummernoteWidget(),
        }
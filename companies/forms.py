from django import forms
from django_summernote.widgets import SummernoteWidget
from talenthub.sanitise import clean_html
from .models import Companies

# form to edit company profile

class CompanyProfileForm(forms.ModelForm):
    class Meta:
        model = Companies
        fields = ['company_name', 'description', 'website', 'sectors']
        widgets = {
            'description': SummernoteWidget(),
            'sectors': SummernoteWidget(),
        }

    def clean_description(self):
        return clean_html(self.cleaned_data['description'])

    def clean_sectors(self):
        return clean_html(self.cleaned_data['sectors'])
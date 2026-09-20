from django import forms
from .models import Companies

class CompanyProfileForm(forms.ModelForm):
    class Meta:
        model = Companies
        fields = ['company_name', 'description', 'website', 'sectors']
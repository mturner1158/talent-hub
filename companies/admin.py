from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin 
from .models import Companies

#enabling summernote fields on Companies model
@admin.register(Companies)
class CompaniesAdmin(SummernoteModelAdmin):
    search_fields = ['company_name']
    list_filter = ('created_on',)
    summernote_fields = ('description', 'sectors',)
    prepopulated_fields = {'slug': ('company_name',)}


# Register your models here.
from django.contrib import admin
from .models import Companies


@admin.register(Companies)
class CompaniesAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'owner', 'created_on')
    search_fields = ['company_name']
    list_filter = ('created_on',)
    prepopulated_fields = {'slug': ('company_name',)}

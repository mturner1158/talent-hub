from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin 
from .models import Job

#enabling summernote fields on Job model
@admin.register(Job)
class JobAdmin(SummernoteModelAdmin):
    list_display = ('title', 'company', 'is_active')
    search_fields = ['title']
    list_filter = ('is_active', 'created_on')
    summernote_fields = ('description',)

# Register your models here.


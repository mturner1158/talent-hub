from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin 
from .models import Candidate

#enabling summernote fields on Companies model
@admin.register(Candidate)
class CandidateAdmin(SummernoteModelAdmin):
    summernote_fields = ('personal_statement', 'skills', 'experience')



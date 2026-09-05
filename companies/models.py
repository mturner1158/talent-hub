from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Companies(models.Model):
    """
    Contains a profile for each company which has signed up for Talent Hub
    """
    company_name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    website = models.CharField()
    sectors = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __string__(self):
        return f"{self.company_name} profile"

    class Meta:
        ordering = ['company_name']

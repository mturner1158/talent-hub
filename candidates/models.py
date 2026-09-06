from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Candidate(models.Model):
    """
    Contains a profile for each candidate who would like to submit a job application
    """
    account = models.ForeignKey(User, on_delete=models.CASCADE, related_name="candidate_profile")
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    personal_statement = models.TextField()
    skills = models.TextField()
    experience = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} candidate profile"
    
    class Meta:
        ordering = ['-created_on']

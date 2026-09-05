from django.db import models
from companies.models import Companies

JOB_TYPE_CHOICES = (
        ('full_time', 'Full-time'),
        ('part_time', 'Part-time'),
        ('contract', 'Contract'),
        ('remote', 'Remote'),
        )

# Create your models here.
class Job(models.Model):
    """
    Contains a job vacancy posted by a company
    """
    title = models.CharField(max_length=200)
    company = models.ForeignKey(Companies, on_delete=models.CASCADE, related_name="jobs")
    description = models.TextField()
    location = models.CharField(max_length=200)
    salary_min = models.PositiveIntegerField
    salary_min = models.PositiveIntegerField(blank=True, null=True)
    salary_max = models.PositiveIntegerField(blank=True, null=True)
    job_type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"{self.title} at {self.company.company_name}"


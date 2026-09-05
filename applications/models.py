from django.db import models
from jobs.models import Job
from candidates.models import Candidate

STATUS_CHOICES = (
        ('submitted', 'Submitted'),
        ('shortlisted', 'Shortlisted'),
        ('rejected', 'Rejected'),
        ('hired', 'Hired'),
    )

# Create your models here.
class Application(models.Model):
    """
    Contains the job submission from a candidate and the status of the application
    """
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name='applications')
    cover_note = models.TextField()
    uk_working_status = models.BooleanField(default=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='received')
    applied_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('job', 'candidate')
        ordering = ['-applied_on']

    def __str__(self):
        return f"{self.candidate} | {self.job.title} - ({self.status})"

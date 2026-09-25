from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
class Companies(models.Model):
    """
    Contains a profile for each company which has signed up for Talent Hub
    """
    company_name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name="company_contact")
    slug = models.CharField(max_length=200, unique=True)
    website = models.URLField(blank=True)
    sectors = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.company_name} profile"

    # solves bug where users choosing company are not linked
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.company_name) or f"company-{self.pk or 'new'}"
            slug = base_slug
            counter = 1
            while Companies.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['company_name']

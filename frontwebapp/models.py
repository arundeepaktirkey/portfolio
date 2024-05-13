from django.db import models

# Create your models here.
class WorkExp(models.Model):
    title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)   
    description = models.TextField(max_length=500)
    skills = models.CharField(max_length=300)

class Education(models.Model):
    degree = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)   
    description = models.TextField(max_length=500)
    skills = models.CharField(max_length=300)
    

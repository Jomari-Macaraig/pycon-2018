from django.db import models

# Create your models here.

class Speaker(models.Model):
    NORMAL = 'n'
    KEYNOTE = 'k'
    CHOICES = (
        (NORMAL, 'Normal'),
        (KEYNOTE, 'Keynote')
    )
    name = models.CharField(max_length=64)
    company_name = models.CharField(max_length=128, blank=True, null=True)
    job_title = models.CharField(max_length=128, blank=True, null=True)
    description = models.TextField()
    image = models.ImageField(upload_to='uploads/speaker')
    speaker_type = models.CharField(max_length=1, default=NORMAL, choices=CHOICES)


class SponsorType(models.Model):
    name = models.CharField(max_length=64)


class Sponsor(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    image = models.ImageField(upload_to='uploads/sponsor')
    sponsor_type = models.ForeignKey(SponsorType)

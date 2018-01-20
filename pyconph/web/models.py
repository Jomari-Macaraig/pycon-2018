from django.db import models

# Create your models here.

class Volunteer(models.Model):
    name = models.CharField(max_length=64)

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

    def __str__(self):
        return self.name


class SponsorType(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Sponsor(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    image = models.ImageField(upload_to='uploads/sponsor')
    link = models.URLField()
    sponsor_type = models.ForeignKey(SponsorType)

    def __str__(self):
        return self.name


class PartnerType(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Partner(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    image = models.ImageField(upload_to='uploads/partner')
    link = models.URLField()
    partner_type = models.ForeignKey(PartnerType)

    def __str__(self):
        return self.name


class Schedule(models.Model):
    DAY1 = 1
    DAY2 = 2
    CHOICES = (
        (DAY1, 'DAY1'),
        (DAY2, 'DAY2')
    )
    name = models.CharField(max_length=64)
    start_time = models.TimeField()
    end_time = models.TimeField()
    description = models.TextField(null=True, blank=True)
    speaker = models.ForeignKey(Speaker, null=True, blank=True)
    day = models.IntegerField(choices=CHOICES, default=DAY1)

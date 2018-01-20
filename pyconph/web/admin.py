from django.contrib import admin

from .models import (
    Volunteer,
    Partner,
    PartnerType,
    Schedule,
    Speaker,
    Sponsor,
    SponsorType
)

class VolunteerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class SpeakerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'speaker_type')

class SponsorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sponsor_type')

class SponsorTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class PartnerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'partner_type')

class PartnerTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('id', 'speaker', 'name', 'start_time', 'end_time', 'day')

admin.site.register(Volunteer, VolunteerAdmin)
admin.site.register(Partner, PartnerAdmin)
admin.site.register(PartnerType, PartnerTypeAdmin)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Speaker, SpeakerAdmin)
admin.site.register(Sponsor, SponsorAdmin)
admin.site.register(SponsorType, SponsorTypeAdmin)

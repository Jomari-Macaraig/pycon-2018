from django.contrib import admin

from .models import Speaker, Sponsor, SponsorType

class SpeakerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'speaker_type')

class SponsorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sponsor_type')

class SponsorTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(Speaker, SpeakerAdmin)
admin.site.register(Sponsor, SponsorAdmin)
admin.site.register(SponsorType, SponsorTypeAdmin)

from django.contrib import admin

from .models import Speaker

class SpeakerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'speaker_type')

admin.site.register(Speaker, SpeakerAdmin)

# Register your models here.

from django.shortcuts import render
from .models import Speaker, Sponsor, SponsorType

# Create your views here.
def index(request):
    speakers = Speaker.objects.all()
    keynotes = speakers.filter(speaker_type=Speaker.KEYNOTE)
    other_speakers = speakers.filter(speaker_type=Speaker.NORMAL)
    sponsors = {}
    for sponsor_type in SponsorType.objects.all().iterator():
        sponsors[sponsor_type.name] = Sponsor.objects.filter(sponsor_type_id=sponsor_type.id)

    context = {
        'keynotes': keynotes,
        'other_speakers': other_speakers,
        'sponsors': sponsors
    }
    return render(request, 'web/index.html', context)

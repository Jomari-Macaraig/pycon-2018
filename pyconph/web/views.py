from django.shortcuts import render
from .models import (
    Partner,
    PartnerType,
    Volunteer,
    Speaker,
    Sponsor,
    SponsorType
)

# Create your views here.
def index(request):
    volunteers = Volunteer.objects.all().order_by('name')
    speakers = Speaker.objects.all()
    keynotes = speakers.filter(speaker_type=Speaker.KEYNOTE)
    other_speakers = speakers.filter(speaker_type=Speaker.NORMAL)
    sponsors = {}
    partners = {}

    for sponsor_type in SponsorType.objects.all().iterator():
        sponsors[sponsor_type.name] = Sponsor.objects.filter(sponsor_type_id=sponsor_type.id)

    for partner_type in PartnerType.objects.all().iterator():
        partners[partner_type.name] = Partner.objects.filter(partner_type_id=partner_type.id)

    context = {
        'keynotes': list(keynotes),
        'other_speakers': other_speakers,
        'sponsors': sponsors,
        'volunteers': volunteers,
        'partners': partners
    }
    return render(request, 'web/index.html', context)

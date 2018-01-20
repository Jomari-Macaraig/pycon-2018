from django.shortcuts import render

from .models import (
    Partner,
    PartnerType,
    Sponsor,
    SponsorType
)

# Create your views here.
def index(request):
    sponsors = {}
    partners = {}

    for sponsor_type in SponsorType.objects.all().iterator():
        sponsors[sponsor_type.name] = Sponsor.objects.filter(sponsor_type_id=sponsor_type.id)

    for partner_type in PartnerType.objects.all().iterator():
        partners[partner_type.name] = Partner.objects.filter(partner_type_id=partner_type.id)

    context = {
        'sponsors': sponsors,
        'partners': partners
    }
    return render(request, 'web/index.html', context)

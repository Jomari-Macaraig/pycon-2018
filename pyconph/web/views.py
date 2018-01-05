from django.shortcuts import render
from .models import Speaker

# Create your views here.
def index(request):
    speakers = Speaker.objects.all()
    keynotes = speakers.filter(speaker_type=Speaker.KEYNOTE)
    other_speakers = speakers.filter(speaker_type=Speaker.NORMAL)
    context = {
        'keynotes': keynotes,
        'other_speakers': other_speakers
    }
    return render(request, 'web/index.html', context)

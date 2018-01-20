from rest_framework.generics import ListAPIView

from .serializers import (
    ScheduleSerializer,
    SpeakerSerializer,
    SponsorTypeSerializer,
)
from pyconph.web.models import (
    Schedule,
    Speaker,
    SponsorType,
)


class ScheduleListAPIView(ListAPIView):
    model = Schedule
    serializer_class = ScheduleSerializer

    def get_queryset(self):
        return self.model.objects.filter(
            day=self.kwargs['day']
        ).order_by('start_time')


class KeynoteListAPIView(ListAPIView):

    model = Speaker
    serializer_class = SpeakerSerializer

    def get_queryset(self):
        return self.model.objects.filter(
            speaker_type=Speaker.KEYNOTE
        )


class NormalSpeakerListAPIView(ListAPIView):

    model = Speaker
    serializer_class = SpeakerSerializer

    def get_queryset(self):
        return self.model.objects.filter(
            speaker_type=Speaker.NORMAL
        )


class SponsorTypeListAPIView(ListAPIView):

    model = SponsorType
    serializer_class = SponsorTypeSerializer

    def get_queryset(self):
        return self.model.objects.all()

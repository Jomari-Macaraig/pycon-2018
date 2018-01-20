from rest_framework.generics import ListAPIView

from .serializers import (
    PartnerSerializer,
    PartnerTypeSerializer,
    ScheduleSerializer,
    SpeakerSerializer,
    SponsorSerializer,
    SponsorTypeSerializer,
)
from pyconph.web.models import (
    Partner,
    PartnerType,
    Schedule,
    Speaker,
    Sponsor,
    SponsorType,
)


class PartnerListAPIView(ListAPIView):

    model = Partner
    serializer_class = PartnerSerializer

    def get_queryset(self):
        return self.model.objects.filter(
            partner_type_id=self.kwargs['partner_type_id']
        )

class PartnerTypeListAPIView(ListAPIView):

    model = PartnerType
    serializer_class = PartnerTypeSerializer

    def get_queryset(self):
        return self.model.objects.all()


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


class SponsorListAPIView(ListAPIView):

    model = Sponsor
    serializer_class = SponsorSerializer

    def get_queryset(self):
        return self.model.objects.filter(
            sponsor_type_id=self.kwargs['sponsor_type_id']
        )

class SponsorTypeListAPIView(ListAPIView):

    model = SponsorType
    serializer_class = SponsorTypeSerializer

    def get_queryset(self):
        return self.model.objects.all()

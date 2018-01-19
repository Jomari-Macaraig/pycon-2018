from rest_framework.generics import ListAPIView

from .serializers import SpeakerSerializer
from pyconph.web.models import Speaker


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

from django.conf.urls import url, include

from rest_framework.urlpatterns import format_suffix_patterns

from .views import KeynoteListAPIView, NormalSpeakerListAPIView


speaker_patterns = format_suffix_patterns([
    url(
        r'keynote/list/',
        KeynoteListAPIView.as_view(),
        name='keynote_list'
    ),
    url(
        r'normal/list/',
        NormalSpeakerListAPIView.as_view(),
        name='normal_list'
    ),
])

urlpatterns = [
    url(r'speakers', include(speaker_patterns, namespace='speakers')),
]

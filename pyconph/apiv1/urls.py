from django.conf.urls import url, include

from rest_framework.urlpatterns import format_suffix_patterns

from .views import (
    KeynoteListAPIView,
    NormalSpeakerListAPIView,
    ScheduleListAPIView,
    SponsorTypeListAPIView,
)


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

schedule_patterns = format_suffix_patterns([
    url(
        r'day/(?P<day>[0-9]+)/',
        ScheduleListAPIView.as_view(),
        name='schedule_list'
    ),
])

sponsor_patterns = format_suffix_patterns([
    url(
        r'type/list/',
        SponsorTypeListAPIView.as_view(),
        name='sponsor_list'
    ),
])

urlpatterns = [
    url(r'speakers', include(speaker_patterns, namespace='speakers')),
    url(r'schedule', include(schedule_patterns, namespace='schedule')),
    url(r'sponsors', include(sponsor_patterns, namespace='sponsors')),
]

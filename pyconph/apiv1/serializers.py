from rest_framework import serializers

from pyconph.web.models import Speaker


class SpeakerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Speaker
        fields = (
            'id',
            'name',
            'company_name',
            'job_title',
            'description',
            'image'
        )

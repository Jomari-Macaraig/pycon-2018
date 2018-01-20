from rest_framework import serializers

from pyconph.web.models import (
    Partner,
    PartnerType,
    Schedule,
    Speaker,
    Sponsor,
    SponsorType,
)


class PartnerSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Partner
        fields = (
            'name',
            'description',
            'image',
            'link',
        )

    def get_image(self, obj):
        return obj.image.url


class PartnerTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = PartnerType
        fields = (
            'id',
            'name'
        )


class ScheduleSerializer(serializers.ModelSerializer):
    speaker = serializers.SerializerMethodField()
    start_time = serializers.SerializerMethodField()
    end_time = serializers.SerializerMethodField()

    class Meta:
        model = Schedule
        fields = (
            'id',
            'name',
            'description',
            'start_time',
            'end_time',
            'day',
            'speaker',
        )

    def get_speaker(self, obj):
        serializer = SpeakerSerializer(obj.speaker, read_only=True)
        return serializer.data

    def get_start_time(self, obj):
        return obj.start_time.strftime('%l:%M%p')

    def get_end_time(self, obj):
        return obj.end_time.strftime('%l:%M%p')


class SpeakerSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Speaker
        fields = (
            'id',
            'name',
            'company_name',
            'job_title',
            'description',
            'image',
        )

    def get_image(self, obj):
        return obj.image.url


class SponsorSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Sponsor
        fields = (
            'name',
            'description',
            'image',
            'link',
        )

    def get_image(self, obj):
        return obj.image.url


class SponsorTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = SponsorType
        fields = (
            'id',
            'name'
        )

from rest_framework import serializers

from .models import CircularBanner, HomeBanner


class HomeBannerSerializer(serializers.ModelSerializer):
    # url = serializers.SerializerMethodField()

    class Meta:
        model = HomeBanner
        fields = ['image', 'alt', 'download_link', 'active', ]

class CircularBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CircularBanner
        fields = ['image', 'alt', 'download_link', 'active', ]

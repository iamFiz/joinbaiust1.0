from rest_framework import response, viewsets
from rest_framework.decorators import action

from .models import CircularBanner, HomeBanner
from .serializers import CircularBannerSerializer, HomeBannerSerializer


class HomeBannerViewSet(viewsets.ModelViewSet):
    serializer_class = HomeBannerSerializer
    queryset = HomeBanner.objects.all()

    @action(methods=['get'], detail=False)
    def active_banner(self, request):
        banner = HomeBanner.objects.get(active=True)
        return response.Response(HomeBannerSerializer(banner).data)


class CircularBannerViewSet(viewsets.ModelViewSet):
    serializer_class = CircularBannerSerializer
    queryset = CircularBanner.objects.all()

    @action(methods=['get'], detail=False)
    def active_banner(self, request):
        banner = CircularBanner.objects.get(active=True)
        return response.Response(CircularBannerSerializer(banner).data)

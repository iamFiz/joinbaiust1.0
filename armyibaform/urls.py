from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic import TemplateView
from django.views.static import serve
from rest_framework.routers import DefaultRouter

from about.views import CircularBannerViewSet, HomeBannerViewSet
from application.models import ApplicantExtraInformation
from application.views import (ApplicantExtraInformationViewset,
                               ApplicationPaymentViewset,
                               ApplicationStatusViewset, ApplicationViewset,
                               SeatPlanListView)
from chat.views import ChatRequestViewset
from newsletter.views import NewsLetterViewset, SubscriberViewset

router = DefaultRouter()
router.register(r'application', ApplicationViewset)
router.register(r'payment', ApplicationPaymentViewset)
router.register(r'status', ApplicationStatusViewset)
router.register(r'subscribers', SubscriberViewset)
router.register(r'newsletter', NewsLetterViewset)
router.register(r'chat', ChatRequestViewset)
router.register(r'extra_information', ApplicantExtraInformationViewset)
router.register(r'home_banner', HomeBannerViewSet)
router.register(r'circular_banner', CircularBannerViewSet)
urlpatterns = []

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += [
    path('api/result/', include('result.urls')),
    re_path(
        r'^seat-plan/(?P<path>.*)$', SeatPlanListView.as_view(), name='seat-plan'),
    # path(
    #     'abc_all/', DhakaApplicationViewAll.as_view(), name='dhakaall'),
    re_path(r'^admin/', admin.site.urls),
    re_path(r"^api/", include(router.urls)),
    re_path(r'^media/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^.*$', TemplateView.as_view(template_name='base.html'), name='frontend')

]

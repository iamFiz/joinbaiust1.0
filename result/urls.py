from django.urls import path

from .views import ResultView

urlpatterns = [
    path('individual/<lookup>/', ResultView.as_view(), name='result'),
]

from django.db.models import Q
from django.shortcuts import render
from rest_framework import generics

from .models import Result
from .serializers import ResultSerializer


class ResultView(generics.RetrieveAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
    model = Result

    def get_object(self):
        lookup = self.kwargs['lookup']
        return Result.objects.get(Q(application__details__serial=lookup) | Q(application__id=lookup))

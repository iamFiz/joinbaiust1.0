from rest_framework import viewsets

from chat.models import ChatRequest

from .serializers import ChatRequestSerializer


class ChatRequestViewset(viewsets.ModelViewSet):
    serializer_class = ChatRequestSerializer
    queryset = ChatRequest.objects.all()

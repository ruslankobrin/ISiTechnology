from rest_framework import generics, serializers

from .models import Thread
from .serializers import ThreadSerializer


class ThreadCreateListView(generics.ListCreateAPIView):
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer

    def perform_create(self, serializer):
        participants = serializer.validated_data.get("participants")
        if len(participants) > 2:
            raise serializers.ValidationError(
                "A thread can't have more than 2 participants"
            )
        serializer.save()


class ThreadRetrieveDeleteView(generics.RetrieveDestroyAPIView):
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer
    lookup_field = "pk"


class ThreadListAPIView(generics.ListAPIView):
    serializer_class = ThreadSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Thread.objects.filter(participants__id=user_id)

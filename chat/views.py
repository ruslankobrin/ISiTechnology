from rest_framework import generics, serializers, status
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

from .models import Thread, Message
from .serializers import ThreadSerializer, MessageSerializer


class ThreadCreateListView(generics.ListCreateAPIView):
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer
    pagination_class = LimitOffsetPagination

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


class MessageCreateListView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        sender = serializer.validated_data.get("sender")
        thread = serializer.validated_data.get("thread")

        if not Thread.objects.filter(id=thread.id, participants=sender).exists():
            raise serializers.ValidationError(
                "You are not this participant in this thread"
            )
        serializer.save()


class MessageRetrieveView(generics.RetrieveAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    lookup_field = "pk"


class MessageMarkAsReadView(generics.UpdateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    lookup_field = "pk"
    http_method_names = ["put"]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_read = True
        instance.save()
        return Response(
            {"message": "Message marked as read"}, status=status.HTTP_200_OK
        )


class UnreadMessageCountView(generics.GenericAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def get(self, request, *args, **kwargs):
        user = self.kwargs.get("user")
        unread_count = Message.objects.filter(
            thread__participants=user, is_read=False
        ).count()
        return Response({"unread_count": unread_count}, status=status.HTTP_200_OK)


class ThreadListAPIView(generics.ListAPIView):
    serializer_class = ThreadSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        user_id = self.kwargs["user_id"]
        return Thread.objects.filter(participants__id=user_id)


class MessageListByThreadAPIView(generics.ListAPIView):
    serializer_class = MessageSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        thread_id = self.kwargs["thread_id"]
        return Message.objects.filter(thread_id=thread_id)

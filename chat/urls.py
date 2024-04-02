from django.urls import path
from .views import *

urlpatterns = [
    path('threads/', ThreadCreateListView.as_view(), name='thread_create_list'),
    path('threads_by_user/<int:user_id>/', ThreadListAPIView.as_view(), name='threads_by_user'),
    path('threads/<int:pk>/', ThreadRetrieveDeleteView.as_view(), name='thread_retrieve_delete'),
    path('messages/', MessageCreateListView.as_view(), name='message_create_list'),
    path('messages/<int:pk>/', MessageRetrieveView.as_view(), name='message_retrieve'),
    path('messages_by_thread/<int:thread_id>/', MessageListByThreadAPIView.as_view(), name='messages_by_thread'),
    path('messages/<int:pk>/read/', MessageMarkAsReadView.as_view(), name='message_mark_as_read'),
    path('unread/<str:user>/', UnreadMessageCountView.as_view(), name='unread_message_count'),
]
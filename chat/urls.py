from django.urls import path
from .views import *

urlpatterns = [
    path('threads/', ThreadCreateListView.as_view(), name='thread_create_list'),
    path('threads_by_user/<int:user_id>/', ThreadListAPIView.as_view(), name='threads_by_user'),
    path('threads/<int:pk>/', ThreadRetrieveDeleteView.as_view(), name='thread_retrieve_delete'),
]
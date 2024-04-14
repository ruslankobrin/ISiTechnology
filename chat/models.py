from django.db import models
from django.contrib.auth.models import User


class Thread(models.Model):
    participants = models.ManyToManyField(User, related_name="threads")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Thread {self.id}"

    class Meta:
        verbose_name = 'Discussion Thread'
        verbose_name_plural = 'Discussion Threads'


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.sender} in Thread {self.thread_id}"

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'

from django.contrib import admin

from chat.models import Thread, Message


@admin.register(Thread)
class ThreadAdmin(admin.ModelAdmin):
    list_display = ("id", "created", "updated")
    list_filter = ("created", "updated")
    search_fields = ("id",)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("id", "sender", "thread", "created", "is_read")
    list_filter = ("created", "is_read")
    search_fields = ("id", "sender__username", "thread__id")


admin.site.site_header = "Chat Admin"
admin.site.site_title = "Chat Admin"

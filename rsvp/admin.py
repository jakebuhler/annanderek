from django.contrib import admin

from rsvp import models


@admin.register(models.Response)
class ResponseAdmin(admin.ModelAdmin):

    list_display = ('name', 'guest_count', 'accommodation_requests', 'submitted')

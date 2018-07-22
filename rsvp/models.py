from __future__ import unicode_literals

from django.db import models

class Response(models.Model):

    name = models.CharField(max_length=128)
    guest_count = models.IntegerField(verbose_name="Number of Guests")
    accommodation_requests = models.TextField(blank=True, verbose_name="Special Accommodations")
    submitted = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('submitted',)

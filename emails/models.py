from django.db import models


class EmailSchedule(models.Model):
    subject = models.CharField(max_length=255)
    body = models.TextField(blank=True)
    to_email = models.EmailField()
    to_name = models.CharField(max_length=255, blank=True)
    from_email = models.EmailField()
    from_name = models.CharField(max_length=255, blank=True)
    scheduled_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
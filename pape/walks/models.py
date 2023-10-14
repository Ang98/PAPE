from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL


class Walk(models.Model):
    walker = models.ForeignKey(User, on_delete=models.CASCADE, related_name="walks_as_walker")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="walks_as_owner")
    scheduled_time = models.DateTimeField()
    start_location = models.CharField(max_length=255)
    end_location = models.CharField(max_length=255)
    status = models.CharField(max_length=20, default="Scheduled")
    duration = models.PositiveIntegerField(null=True, blank=True)  # Duration in minutes


class WalkLocation(models.Model):
    walk = models.ForeignKey(Walk, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)


class WalkHistory(models.Model):
    walk = models.ForeignKey(Walk, on_delete=models.CASCADE)
    completed_time = models.DateTimeField()
    distance = models.DecimalField(max_digits=6, decimal_places=2)
    walker_rating = models.PositiveIntegerField(default=0)
    owner_rating = models.PositiveIntegerField(default=0)


class InsuranceClaim(models.Model):
    walk = models.ForeignKey(Walk, on_delete=models.CASCADE)
    claimant = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    claim_status = models.CharField(max_length=20, default="Pending")


# Add other fields and relationships as needed.

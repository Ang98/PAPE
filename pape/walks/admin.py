from django.contrib import admin

from .models import InsuranceClaim, Walk, WalkHistory, WalkLocation


@admin.register(Walk)
class WalkAdmin(admin.ModelAdmin):
    list_display = ("walker", "owner", "scheduled_time", "status")
    list_filter = ("status",)
    search_fields = ("walker__username", "owner__username")


@admin.register(WalkLocation)
class WalkLocationAdmin(admin.ModelAdmin):
    list_display = ("walk", "timestamp", "latitude", "longitude")
    search_fields = ("walk__walker__username",)


@admin.register(WalkHistory)
class WalkHistoryAdmin(admin.ModelAdmin):
    list_display = ("walk", "completed_time", "distance", "walker_rating", "owner_rating")
    search_fields = ("walk__walker__username", "walk__owner__username")


@admin.register(InsuranceClaim)
class InsuranceClaimAdmin(admin.ModelAdmin):
    list_display = ("walk", "claimant", "claim_status")
    list_filter = ("claim_status",)
    search_fields = ("walk__walker__username", "claimant__username")

from django.contrib import admin

from .models import WalkerProfile, WalkerReview


@admin.register(WalkerProfile)
class WalkerProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "experience", "availability")
    list_filter = ("availability",)
    search_fields = ("user__username",)


@admin.register(WalkerReview)
class WalkerReviewAdmin(admin.ModelAdmin):
    list_display = ("walker", "reviewer", "rating")
    list_filter = ("rating",)
    search_fields = ("walker__user__username", "reviewer__username")

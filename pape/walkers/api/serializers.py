from rest_framework import serializers

from ..models import WalkerProfile, WalkerReview


class WalkerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = WalkerProfile
        fields = "__all__"


class WalkerReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = WalkerReview
        fields = "__all__"


# Add other serializers if needed.

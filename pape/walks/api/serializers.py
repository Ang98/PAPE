from rest_framework import serializers

from ..models import InsuranceClaim, Walk, WalkHistory, WalkLocation


class WalkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Walk
        fields = "__all__"


class WalkLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = WalkLocation
        fields = "__all__"


class WalkHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = WalkHistory
        fields = "__all__"


class InsuranceClaimSerializer(serializers.ModelSerializer):
    class Meta:
        model = InsuranceClaim
        fields = "__all__"


# Add other serializers if needed.

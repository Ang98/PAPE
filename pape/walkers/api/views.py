from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from ..models import WalkerProfile, WalkerReview
from .serializers import WalkerProfileSerializer, WalkerReviewSerializer


class WalkerProfileViewSet(viewsets.ModelViewSet):
    queryset = WalkerProfile.objects.all()
    serializer_class = WalkerProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=["PUT"])
    def set_availability(self, request):
        # Logic to set the availability of the walker
        walker_profile = request.user.walkerprofile
        availability = request.data.get("availability", False)
        walker_profile.availability = availability
        walker_profile.save()
        return Response({"message": "Availability updated"}, status=status.HTTP_200_OK)


class WalkerReviewViewSet(viewsets.ModelViewSet):
    queryset = WalkerReview.objects.all()
    serializer_class = WalkerReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request):
        # Logic to create a review with a rating and comment
        walker_profile_id = request.data.get("walker_profile")
        rating = request.data.get("rating")
        comment = request.data.get("comment")

        walker_review = WalkerReview.objects.create(
            walker_id=walker_profile_id, reviewer=request.user, rating=rating, comment=comment
        )
        walker_review.save()
        return Response({"message": "Review created"}, status=status.HTTP_201_CREATED)

    # Implement other actions or overrides as needed.

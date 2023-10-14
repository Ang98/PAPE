from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from ..models import InsuranceClaim, Walk, WalkHistory, WalkLocation
from .serializers import InsuranceClaimSerializer, WalkHistorySerializer, WalkLocationSerializer, WalkSerializer


class WalkViewSet(viewsets.ModelViewSet):
    queryset = Walk.objects.all()
    serializer_class = WalkSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=["POST"])
    def schedule_walk(self, request):
        # Logic to schedule a walk with details like scheduled_time, start_location, end_location, etc.
        # Return the created walk object.
        serializer = WalkSerializer(data=request.data)
        if serializer.is_valid():
            walk = serializer.save()
            return Response(WalkSerializer(walk).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=["GET"])
    def track_walk(self, request, pk=None):
        # Logic to retrieve the location data for a specific walk, including latitude and longitude.
        walk = self.get_object()
        locations = WalkLocation.objects.filter(walk=walk)
        serializer = WalkLocationSerializer(locations, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["POST"])
    def complete_walk(self, request, pk=None):
        # Logic to mark a walk as completed, calculate distance, and gather rating information.
        walk = self.get_object()
        walk.status = "Completed"
        walk.duration = request.data.get("duration")
        walk.save()

        history = WalkHistory.objects.create(
            walk=walk,
            completed_time=walk.scheduled_time,
            distance=request.data.get("distance"),
            walker_rating=request.data.get("walker_rating"),
            owner_rating=request.data.get("owner_rating"),
        )
        history.save()


class WalkLocationViewSet(viewsets.ModelViewSet):
    queryset = WalkLocation.objects.all()
    serializer_class = WalkLocationSerializer
    permission_classes = [permissions.IsAuthenticated]


class WalkHistoryViewSet(viewsets.ModelViewSet):
    queryset = WalkHistory.objects.all()
    serializer_class = WalkHistorySerializer
    permission_classes = [permissions.IsAuthenticated]


class InsuranceClaimViewSet(viewsets.ModelViewSet):
    queryset = InsuranceClaim.objects.all()
    serializer_class = InsuranceClaimSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=["POST"])
    def report_issue(self, request, pk=None):
        # Logic to report an issue during a walk, create a claim, and update claim status.
        walk = self.get_object()
        claimant = request.user
        description = request.data.get("description")

        claim = InsuranceClaim.objects.create(walk=walk, claimant=claimant, description=description)
        claim.save()

        return Response(InsuranceClaimSerializer(claim).data, status=status.HTTP_201_CREATED)


# Additional views for managing walk schedules, tracking, and reporting issues.

# Define URL routes in your urls.py.

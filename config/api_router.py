from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from pape.users.api.views import PasswordResetView, UserCreateViewSet, UserDeleteViewSet, UserViewSet
from pape.walkers.api.views import WalkerProfileViewSet, WalkerReviewViewSet
from pape.walks.api.views import InsuranceClaimViewSet, WalkHistoryViewSet, WalkLocationViewSet, WalkViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

# users
router.register("users", UserViewSet, basename="users")
router.register("users_create", UserCreateViewSet, basename="users_create")
router.register("users_delete", UserDeleteViewSet, basename="users_delete")
router.register("users_password", PasswordResetView, basename="users_password")

# walkers
router.register("walkers_review", WalkerReviewViewSet, basename="walkers_review")
router.register("walkers_profile", WalkerProfileViewSet, basename="walkers_profile")

# walks

router.register("walks", WalkViewSet, basename="walks")
router.register("walks_history", WalkHistoryViewSet, basename="walks_history")
router.register("walks_location", WalkLocationViewSet, basename="walks_location")
router.register("walks_insurance", InsuranceClaimViewSet, basename="walks_insurance")


app_name = "api"
urlpatterns = router.urls

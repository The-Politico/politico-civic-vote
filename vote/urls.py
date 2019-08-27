# Imports from Django.
from django.urls import include
from django.urls import path

# Imports from other dependencies.
from rest_framework import routers

# Imports from vote.
from vote.viewsets import DelegatesViewSet
from vote.viewsets import ElectoralVotesViewSet
from vote.viewsets import VotesViewSet


router = routers.DefaultRouter()

router.register(r"delegates", DelegatesViewSet)
router.register(r"electoral-votes", ElectoralVotesViewSet)
router.register(r"votes", VotesViewSet)


urlpatterns = [path("api/", include(router.urls))]

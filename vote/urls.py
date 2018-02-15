from django.urls import include, path
from rest_framework import routers

from .viewsets import DelegatesViewSet, ElectoralVotesViewSet, VotesViewSet

router = routers.DefaultRouter()

router.register(r'delegates', DelegatesViewSet)
router.register(r'electoral-votes', ElectoralVotesViewSet)
router.register(r'votes', VotesViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
]

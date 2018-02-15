from vote.models import Votes
from vote.serializers import VotesSerializer

from .base import BaseViewSet


class VotesViewSet(BaseViewSet):
    queryset = Votes.objects.all()
    serializer_class = VotesSerializer

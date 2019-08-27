# Imports from vote.
from vote.models import ElectoralVotes
from vote.serializers import ElectoralVotesSerializer
from vote.viewsets.base import BaseViewSet


class ElectoralVotesViewSet(BaseViewSet):
    queryset = ElectoralVotes.objects.all()
    serializer_class = ElectoralVotesSerializer

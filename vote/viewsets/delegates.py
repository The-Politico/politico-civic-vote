# Imports from vote.
from vote.models import Delegates
from vote.serializers import DelegatesSerializer
from vote.viewsets.base import BaseViewSet


class DelegatesViewSet(BaseViewSet):
    queryset = Delegates.objects.all()
    serializer_class = DelegatesSerializer

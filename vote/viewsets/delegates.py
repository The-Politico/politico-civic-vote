from vote.models import Delegates
from vote.serializers import DelegatesSerializer

from .base import BaseViewSet


class DelegatesViewSet(BaseViewSet):
    queryset = Delegates.objects.all()
    serializer_class = DelegatesSerializer

# Imports from python.
import uuid


# Imports from Django.
from django.db import models


# Imports from other dependencies.
from civic_utils.models import CivicBaseModel
from civic_utils.models import UUIDMixin
from geography.models import Division


class BaseResult(UUIDMixin, CivicBaseModel):
    """Abstract result class."""

    division = models.ForeignKey(
        Division, related_name="+", on_delete=models.PROTECT
    )
    count = models.PositiveIntegerField()
    pct = models.DecimalField(
        decimal_places=3, max_digits=5, blank=True, null=True
    )
    total = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        abstract = True

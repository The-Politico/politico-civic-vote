import uuid

from django.db import models
from geography.models import Division


class BaseResult(models.Model):
    """Abstract result class."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    division = models.ForeignKey(
        Division, related_name="+",
        on_delete=models.PROTECT
    )
    count = models.PositiveIntegerField()
    pct = models.DecimalField(
        decimal_places=3, max_digits=5, blank=True, null=True)
    total = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        abstract = True

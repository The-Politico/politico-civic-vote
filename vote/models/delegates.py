from django.db import models
from election.models import CandidateElection

from .base_result import BaseResult


class Delegates(BaseResult):
    """Pledged delegates."""
    candidate_election = models.ForeignKey(
        CandidateElection,
        null=True, blank=True, related_name="delegates",
        on_delete=models.PROTECT
    )
    superdelegates = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Delegates"

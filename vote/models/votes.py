from django.db import models
from election.models import BallotAnswer, CandidateElection

from .base_result import BaseResult


class Votes(BaseResult):
    """Popular vote results."""
    candidate_election = models.ForeignKey(
        CandidateElection,
        null=True, blank=True, related_name="votes",
        on_delete=models.PROTECT
    )
    ballot_answer = models.ForeignKey(
        BallotAnswer,
        null=True, blank=True,
        on_delete=models.PROTECT
    )
    winning = models.BooleanField(default=False)

    def __str__(self):
        return '{0} {1} {2}'.format(
            self.candidate_election.candidate.person.last_name,
            self.candidate_election.election,
            self.division
        )

    class Meta:
        verbose_name_plural = "Votes"

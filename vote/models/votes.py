# Imports from Django.
from django.db import models


# Imports from other dependencies.
from election.models import BallotAnswer
from election.models import CandidateElection


# Imports from vote.
from vote.models.base_result import BaseResult


class Votes(BaseResult):
    """Popular votes."""

    candidate_election = models.ForeignKey(
        CandidateElection,
        null=True,
        blank=True,
        related_name="votes",
        on_delete=models.PROTECT,
    )
    ballot_answer = models.ForeignKey(
        BallotAnswer, null=True, blank=True, on_delete=models.PROTECT
    )
    winning = models.BooleanField(default=False)
    runoff = models.BooleanField(default=False)

    def __str__(self):
        return "{0} {1} {2}".format(
            self.candidate_election.candidate.person.last_name,
            self.candidate_election.election,
            self.division,
        )

    class Meta:
        verbose_name_plural = "Votes"

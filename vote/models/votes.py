# Imports from Django.
from django.db import models


# Imports from other dependencies.
from civic_utils.models import UniqueIdentifierMixin
from election.models import BallotAnswer
from election.models import CandidateElection


# Imports from vote.
from vote.models.base_result import BaseResult


class Votes(UniqueIdentifierMixin, BaseResult):
    """Popular votes."""

    natural_key_fields = ["ballot_answer", "candidate_election", "division"]
    uid_prefix = "votes"
    default_serializer = "vote.serializers.VotesSerializer"

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

    class Meta:
        unique_together = ("ballot_answer", "candidate_election", "division")
        verbose_name_plural = "Votes"

    def __str__(self):
        return "{0} {1} {2}".format(
            self.candidate_election.candidate.person.last_name,
            self.candidate_election.election,
            self.division,
        )

    def save(self, *args, **kwargs):
        """
        **uid field**: :code:`votes:{division uid}`
        **identifier**: :code:`<candidate election uid>__<this uid>` OR
        :code:`<ballot answer uid>__<this uid>`
        """
        self.generate_unique_identifier()

        super(Votes, self).save(*args, **kwargs)

    def get_uid_prefix(self):
        if self.ballot_answer:
            return "{self.ballot_answer.uid}__{self.uid_prefix}"
        return "{self.candidate_election.uid}__{self.uid_prefix}"

    def get_uid_base_field(self):
        return self.division.get_uid_suffix()

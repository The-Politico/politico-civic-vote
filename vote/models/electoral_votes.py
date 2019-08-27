# Imports from Django.
from django.db import models


# Imports from other dependencies.
from civic_utils.models import UniqueIdentifierMixin
from election.models import CandidateElection


# Imports from vote.
from vote.models.base_result import BaseResult


class ElectoralVotes(UniqueIdentifierMixin, BaseResult):
    """Electoral votes."""

    natural_key_fields = ["candidate_election", "division"]
    uid_prefix = "electoral_votes"
    default_serializer = "vote.serializers.ElectoralVotesSerializer"

    candidate_election = models.ForeignKey(
        CandidateElection,
        null=True,
        blank=True,
        related_name="electoral_votes",
        on_delete=models.PROTECT,
    )
    winning = models.BooleanField(default=False)

    class Meta:
        unique_together = ("candidate_election", "division")
        verbose_name_plural = "Electoral Votes"

    def save(self, *args, **kwargs):
        """
        **uid field**: :code:`electoral_votes:{division uid}`
        **identifier**: :code:`<candidate election uid>__<this uid>`
        """
        self.generate_unique_identifier()

        super(ElectoralVotes, self).save(*args, **kwargs)

    def get_uid_prefix(self):
        return "{self.candidate_election.uid}__{self.uid_prefix}"

    def get_uid_base_field(self):
        return self.division.get_uid_suffix()

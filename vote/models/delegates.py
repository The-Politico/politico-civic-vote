# Imports from Django.
from django.db import models


# Imports from other dependencies.
from civic_utils.models import UniqueIdentifierMixin
from election.models import CandidateElection


# Imports from vote.
from vote.models.base_result import BaseResult


class Delegates(UniqueIdentifierMixin, BaseResult):
    """Pledged delegates."""

    natural_key_fields = ["candidate_election", "division"]
    uid_prefix = "delegates"
    default_serializer = "vote.serializers.DelegatesSerializer"

    candidate_election = models.ForeignKey(
        CandidateElection,
        null=True,
        blank=True,
        related_name="delegates",
        on_delete=models.PROTECT,
    )
    superdelegates = models.BooleanField(default=False)

    class Meta:
        unique_together = ("candidate_election", "division")
        verbose_name_plural = "Delegates"

    def save(self, *args, **kwargs):
        """
        **uid field**: :code:`delegates:{division uid}`
        **identifier**: :code:`<candidate election uid>__<this uid>`
        """
        self.generate_unique_identifier()

        super(Delegates, self).save(*args, **kwargs)

    def get_uid_prefix(self):
        return "{self.candidate_election.uid}__{self.uid_prefix}"

    def get_uid_base_field(self):
        return self.division.get_uid_suffix()

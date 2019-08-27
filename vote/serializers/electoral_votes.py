# Imports from other dependencies.
from rest_framework import serializers


# Imports from vote.
from vote.models import ElectoralVotes


class ElectoralVotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElectoralVotes
        fields = "__all__"

# Imports from other dependencies.
from rest_framework import serializers


# Imports from vote.
from vote.models import Votes


class VotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Votes
        fields = "__all__"

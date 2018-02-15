from rest_framework import serializers
from vote.models import ElectoralVotes


class ElectoralVotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElectoralVotes
        fields = '__all__'

# Imports from other dependencies.
from rest_framework import serializers


# Imports from vote.
from vote.models import Delegates


class DelegatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Delegates
        fields = "__all__"

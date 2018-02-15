from rest_framework import serializers
from vote.models import Delegates


class DelegatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Delegates
        fields = '__all__'

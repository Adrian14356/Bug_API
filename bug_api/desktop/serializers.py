from .models import Bug
from rest_framework import serializers


class BugsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bug
        fields = "__all__"
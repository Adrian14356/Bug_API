from rest_framework.serializers import Serializer, ModelSerializer
from .models import Bug


class BugsSerializer(ModelSerializer):
    class Meta:
        model = Bug
        fields = "__all__"
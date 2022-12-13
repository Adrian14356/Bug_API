from .serializers import BugsSerializer
from rest_framework.viewsets import generics
from .models import Bug

class GetAllBugs(generics.ListAPIView):
    serializer_class = BugsSerializer
    queryset = Bug.objects.all()

from django.shortcuts import render
from .models import Bug
from django.views.generic.detail import DetailView
from rest_framework.generics import ListAPIView
from .serializers import BugsSerializer
from django.contrib import messages

def home(request):
    return render(request, 'desktop/home.html', { 'bugs' : Bug.objects.all() })

class BugsListView(ListAPIView):
    model = Bug
    serializer_class = BugsSerializer

    def get_queryset(self,request):

            project_id = self.request.GET.get("project")
            user_id = self.request.GET.get("user")

            if user_id and project_id is None:
                messages.warning(request, "404")
                bugs = []

                if user_id and project_id is not None:
                    messages.success(f"Project id {Bug.project}, user id {Bug.user}, bug {Bug.description}")

            elif project_id is None:
                messages.warning(request, "404")
                bugs = Bug.object.filter(user__id=user_id).all()

                if bugs is not None:
                    messages.success(f"Project id {bugs.project}, bug {bugs.description}")

            elif user_id is None:

                messages.warning(request, "404")
                bugs = Bug.object.filter(project__id=project_id).all()

                if bugs is not None:
                    messages.success(f"User id {bugs.user}, bug {bugs.description}")

            else:
                bugs = Bug.object.filter(project__id = project_id, user__id=user_id).all()

            return bugs



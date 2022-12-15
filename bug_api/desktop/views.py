from django.shortcuts import render
from .models import Bug
from django.views.generic.detail import DetailView
from rest_framework.generics import ListAPIView
from .serializers import BugsSerializer
from django.contrib import messages
from django.http import HttpResponse





def home(request):
    return render(request, 'desktop/home.html', { 'bugs' : Bug.objects.all() })

class BugsListView(ListAPIView):
    model = Bug
    serializer_class = BugsSerializer

    def get_queryset(self):

            project_id = self.request.GET.get("project")
            user_id = self.request.GET.get("user")

            if user_id and project_id is None:

                bugs = []

                if user_id and project_id is not None:
                    return HttpResponse(f"Project id {Bug.project}, user id {Bug.user}, bug {Bug.description}",
                                        content_type = "desktop/home.html")

            elif project_id is None:
                HttpResponse("404", "desktop/home.html")
                bugs = Bug.objects.filter(user__id=user_id).all()

                if bugs is not None:
                    return HttpResponse(f"Project id {Bug.project}, bug {Bug.description}", content_type = "desktop/home.html")

            elif user_id is None:

                HttpResponse("404", content_type = "desktop/home.html")
                bugs = Bug.objects.filter(project__id=project_id).all()

                if bugs is not None:
                    return HttpResponse(f"User id {Bug.user}, bug {Bug.description}", content_type = "desktop/home.html" )

            else:

                return HttpResponse("404", content_type = "desktop/home.html")


            return bugs

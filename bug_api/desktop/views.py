from django.shortcuts import render
from .models import Bug
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView



def home(request):
    return render(request, 'desktop/home.html', { 'bugs' : Bug.objects.all() })

class BugsListView(ListView):
    model = Bug
    template_name = "desktop/home.html"
    context_object_name = "bugs"

    def bugs(self, request):
        if request.method == "GET":
            project = request.GET["project"]
            user = request.GET["user"]

            if user and project is None:
                print("404 error")
            elif user is None:
                print("404")
            elif project is None:
                print("404")
            else:
                print(user)

        return render(request, "desktop/home.html")


class BugsDetailView(DetailView):
    model = Bug
    template_name = "desktop/bugs.html"





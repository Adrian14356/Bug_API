
from django.urls import path
from .views import *
from .serializers_view import *

urlpatterns = [
    path('', BugsListView.as_view(), name = "home"),
    path("bug/", BugsListView.as_view(), name = "bugs-detail"), # /bugs/3, /bugs?project_id=10
    path("bugs/", GetAllBugs.as_view(), name = "get_bugs")
    ]
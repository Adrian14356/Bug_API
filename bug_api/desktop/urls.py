
from django.urls import path
from .views import BugsListView, BugsDetailView

urlpatterns = [
    path('', BugsListView.as_view(), name = "home"),
    path("bugs/<int:pk>/", BugsListView.as_view(), name = "bugs-detail"),
    ]
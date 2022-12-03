from django.urls import path
from .views import HomeListView, SearchResultsListView, ToursList

app_name = "store"


urlpatterns = [
    path("home/", HomeListView.as_view(), name="home"),
    path("search/", SearchResultsListView.as_view(), name="search_results"),
    path("<uuid:pk>/", ToursList, name="details")
]
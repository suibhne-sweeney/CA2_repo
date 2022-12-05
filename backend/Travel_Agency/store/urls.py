from django.urls import path
from .views import SearchResultsListView, ToursAndHotelsList, HomeList, TourDetailView

app_name = "store"


urlpatterns = [
    path("home/", HomeList, name="home"),
    path("search/", SearchResultsListView.as_view(), name="search_results"),
    path("options/<uuid:pk>/", ToursAndHotelsList, name="details"),
    path("<uuid:pk>/", TourDetailView.as_view(), name="tours")
]
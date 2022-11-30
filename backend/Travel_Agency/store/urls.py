from django.urls import path
from .views import PackageListView

urlpatterns = [
    path("home/", PackageListView.as_view(), name="home")
]
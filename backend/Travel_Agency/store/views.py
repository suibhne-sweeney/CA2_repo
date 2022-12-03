from django.shortcuts import render
from django.views.generic import ListView, TemplateView, CreateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import Package, Hotel, Category, Tour, Destination
from django.db.models import Q
# Create your views here.

class HomeListView(ListView):
    model = Destination
    template_name = "shop/index.html"
    context_object_name = "destinations"

def ToursList(request, pk):
    related_tours = []
    destination = Destination.objects.get(pk=pk)
    place = destination.city
    print(place)
    tours = Tour.objects.all()
    for tour in tours:
        if tour.city == place:
            related_tours.append(tour)

    context = {"tours": related_tours}
    return render(request, "shop/details.html", context)


class SearchResultsListView(ListView):
    context_object_name = "objects"
    template_name = "shop/search_results.html"

    def get_queryset(self):
        lst = []
        query = self.request.GET.get("q")
        destinations = Destination.objects.filter(Q(country__icontains=query) | Q(city__icontains=query))
        hotels = Hotel.objects.filter(Q(name__icontains=query) | Q(city__icontains=query))
        tours = Tour.objects.filter(Q(name__icontains=query) | Q(city__icontains=query))
        for destination in destinations:
            lst.append(destination)
        for hotel in hotels:
            lst.append(hotel)
        for tour in tours:
            lst.append(tour)
        return lst


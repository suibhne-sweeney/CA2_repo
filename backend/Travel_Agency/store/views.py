from django.shortcuts import render
from django.views.generic import ListView, TemplateView, CreateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import Location
# Create your views here.

class LocationListView(ListView):
    model = Location
    template_name = "index.html"
    context_object_name = "location"
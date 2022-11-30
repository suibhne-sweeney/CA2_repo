from django.shortcuts import render
from django.views.generic import ListView, TemplateView, CreateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import Package
# Create your views here.

class PackageListView(ListView):
    model = Package
    template_name = "shop/index.html"
    context_object_name = "packages"
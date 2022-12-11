from django.shortcuts import render
from shop.models import Product
from django.views.generic import ListView
from django.db.models import Q
# Create your views here.

class SearchResultsListView(ListView):
    model = Product
    context_object_name = "product_list"
    template_name = "search.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        return Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))

    def get_context_data(self, **kwargs):
        context = super(SearchResultsListView, self).get_context_data(**kwargs)
        context["query"] = self.request.GET.get("q")
        return context
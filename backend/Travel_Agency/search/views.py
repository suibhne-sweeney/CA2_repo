from django.shortcuts import render
from shop.models import Product, Category
from django.db.models import Q

def filterView(request):
    categories = Category.objects.all()
    qs = Product.objects.all()
    title_contains_query = request.GET.get("title_contains")
    id_exact_query = request.GET.get("id_exact")
    star_rating_query = request.GET.get("star_rating")
    category_query = request.GET.get("category")
    avalable_query = request.GET.get("avalable")

    if title_contains_query != "" and title_contains_query is not None:
        qs = qs.filter(Q(name__icontains=title_contains_query))

    elif id_exact_query != "" and id_exact_query is not None:
        qs = qs.filter(Q(id=id_exact_query))

    elif star_rating_query != "" and star_rating_query is not None:
        qs = qs.filter(Q(star_rating__icontains=star_rating_query))
    
    elif category_query != "" and category_query is not None:
        qs = qs.filter(Q(category__name=category_query))

    print(qs)
    context = {
        "queryset": qs,
        "categories": categories
    }
    return render(request, "search_adv.html", context)
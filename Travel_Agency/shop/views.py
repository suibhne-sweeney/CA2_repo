from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.core.paginator import Paginator, EmptyPage, InvalidPage
import random
# Create your views here.

def prod_list(request, category_id=None):
    category = None
    products = Product.objects.filter(available=True)
    if category_id:
        category = get_object_or_404(Category, id=category_id)
        products = Product.objects.filter(category=category, available=True)
    
    paginator = Paginator(products, 6)
    try:
        page = int(request.GET.get("page", "1"))
    except:
        page = 1
    try:
        products = paginator.page(page)
    except(EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pages)
    return render(request, "shop/category.html", {"category": category, "prods": products})

def product_detail(request, category_id, product_id):
    lst = []
    picked_product = Product.objects.get(pk=product_id)
    print(picked_product.destination)
    related_products = Product.objects.all()
    for related_product in related_products:
        print(related_product.name)
        if related_product.name == picked_product.name:
            pass
        elif related_product.destination == picked_product.destination:
            lst.append(related_product)
    product = get_object_or_404(Product, category_id=category_id, id=product_id)
    print(lst)
    start = random.randint(0, len(lst))
    print(start)

    return render(request, "shop/product.html", {"product": product, "related": lst[start:start+4]})


from .models import Category

def menu_links(requset):
    links = Category.objects.all()
    return {"links": links}
from django.shortcuts import render
from .models import ProductCategory, Product, ContactCategory, Contact
import pathlib
import json

# Create your views here.

with open(f'{pathlib.Path().absolute()}/mainapp/templates/mainapp/json/menu.json', 'r') as read_file:
    links_menu = json.load(read_file)

with open(f'{pathlib.Path().absolute()}/mainapp/templates/mainapp/json/categories.json', 'r') as read_file:
    links_categories_menu = json.load(read_file)


def main(request):
    title = 'Домой'

    products = Product.objects.all()[:2]

    content = {
        'title': title,
        'products': products,
        'links_menu': links_menu
    }
    return render(request, 'mainapp/index.html', content)


def products(request, pk=None):
    print(pk)
    title = 'Продукты'

    products = Product.objects.all()[2:5]
    slider_prods = Product.objects.all()[5:8]

    content = {
        'title': title,
        'products': products,
        'slider_prods': slider_prods,
        'links_categories_menu': links_categories_menu,
        'links_menu': links_menu
    }
    return render(request, 'mainapp/products.html', content)


def contact(request):
    title = 'Продукты'

    contacts = Contact.objects.all()[:3]

    content = {
        'title': title,
        'contacts': contacts,
        'links_menu': links_menu
    }
    return render(request, 'mainapp/contact.html', content)

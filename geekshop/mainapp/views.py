from django.shortcuts import render
import pathlib
import json

# Create your views here.

with open(f'{pathlib.Path().absolute()}/mainapp/templates/mainapp/json/menu.json', 'r') as read_file:
    links_menu = json.load(read_file)

with open(f'{pathlib.Path().absolute()}/mainapp/templates/mainapp/json/categories.json', 'r') as read_file:
    links_categories_menu = json.load(read_file)


def main(request):
    content = {
        'title': 'Домой',
        'links_menu': links_menu
    }
    return render(request, 'mainapp/index.html', content)


def products(request):
    content = {
        'title': 'Продукты',
        'links_categories_menu': links_categories_menu,
        'links_menu': links_menu
    }
    return render(request, 'mainapp/products.html', content)


def contact(request):
    content = {
        'title': 'Контакты',
        'links_menu': links_menu
    }
    return render(request, 'mainapp/contact.html', content)

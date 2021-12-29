from django.shortcuts import render
from .models import ProductCategory, Product, Contact
from django.shortcuts import get_object_or_404
from basketapp.models import Basket
import pathlib
import json
import random

# Create your views here.

with open(f'{pathlib.Path().absolute()}/mainapp/json/main_menu.json', 'r') as read_file:
    links_menu = json.load(read_file)

with open(f'{pathlib.Path().absolute()}/mainapp/json/categories.json', 'r') as read_file:
    qwe = json.load(read_file)


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
    title = 'продукты'
    links_categories_menu = ProductCategory.objects.all()
    basket = get_basket(request.user)
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')

        content = {
            'title': title,
            'products': products,
            'category': category,
            'basket': basket,
            'links_categories_menu': links_categories_menu,
            'links_menu': links_menu
        }
        return render(request, 'mainapp/products_list.html', content)

    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)
    content = {
        'title': title,
        'hot_product': hot_product,
        'same_products': same_products,
        'links_categories_menu': links_categories_menu,
        'links_menu': links_menu,
        'basket': basket,
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


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []


def get_hot_product():
    products = Product.objects.all()

    return random.sample(list(products), 1)[0]


def get_same_products(hot_product):
    same_products = Product.objects.filter(category=hot_product.category).exclude(pk=hot_product.pk)[:3]

    return same_products


def product(request, pk):
    title = 'продукты'

    content = {
        'title': title,
        'links_menu': ProductCategory.objects.all(),
        'product': get_object_or_404(Product, pk=pk),
        'basket': get_basket(request.user),
    }

    return render(request, 'mainapp/product.html', content)

from django.shortcuts import render
from .models import ProductCategory, Product
from django.shortcuts import get_object_or_404
from basketapp.models import Basket
import pathlib
import json
import random
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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


def products(request, pk=None, page=1):
    title = 'продукты'
    links_categories_menu = ProductCategory.objects.filter(is_active=True)

    if pk is not None:
        if pk == '0':
            products = Product.objects.filter(is_active=True, category__is_active=True).order_by('price')
            category = {
                'pk': 0,
                'name': 'все'
            }
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk, is_active=True,
                                              category__is_active=True).order_by('price')

        paginator = Paginator(products, 2)
        try:
            products_paginator = paginator.page(page)
        except PageNotAnInteger:
            products_paginator = paginator.page(1)
        except EmptyPage:
            products_paginator = paginator.page(paginator.num_pages)

        content = {
            'title': title,
            'products': products_paginator,
            'category': category,
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
    }
    return render(request, 'mainapp/products.html', content)


def contact(request):
    title = 'Продукты'
    contacts = [
        {'city': 'Москва',
         'phone': '+7-888-444-7777',
         'email': 'info@geekshop.ru',
         'address': 'В пределах МКАД'},
        {'city': 'Санкт-Петербург',
         'phone': '+7-888-333-9999',
         'email': 'info.spb@geekshop.ru',
         'address': 'В пределах КАД'},
        {'city': 'Хабаровск',
         'phone': '+7-888-222-3333',
         'email': 'info.east@geekshop.ru',
         'address': 'В пределах центра'},
    ]
    content = {
        'title': title,
        'contacts': contacts,
        'links_menu': links_menu,
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

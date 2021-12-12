from django.core.management.base import BaseCommand
from mainapp.models import ProductCategory, Product, ContactCategory, Contact
from django.contrib.auth.models import User
from authapp.models import ShopUser
import os
import json

JSON_PATH = 'mainapp/json'


def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r', encoding='utf-8') as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = load_from_json('categories')
        ProductCategory.objects.all().delete()
        for category in categories:
            new_category = ProductCategory(**category)
            new_category.save()

        contacts_category = load_from_json('contacts_category')
        ContactCategory.objects.all().delete()
        for contact in contacts_category:
            new_category_contact = ContactCategory(**contact)
            new_category_contact.save()

        products = load_from_json('products')
        Product.objects.all().delete()
        for product in products:
            category_name = product['category']
            _category = ProductCategory.objects.get(name=category_name)
            product['category'] = _category
            new_product = Product(**product)
            new_product.save()

        contacts = load_from_json('contacts')
        Contact.objects.all().delete()
        for contact in contacts:
            category_alias = contact['category']
            _contact = ContactCategory.objects.get(name=category_alias)
            contact['category'] = _contact
            new_contact = Contact(**contact)
            new_contact.save()

        super_user = ShopUser.objects.create_superuser('django', 'django@geekshop.local', 'geekbrains', age=33)

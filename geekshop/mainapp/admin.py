from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import ProductCategory, Product, ContactCategory, Contact

admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(ContactCategory)
admin.site.register(Contact)

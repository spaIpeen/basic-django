from django.db import models

# Create your models here.


class ProductCategory(models.Model):
    name = models.CharField(verbose_name='имя', max_length=64, unique=True)
    description = models.TextField(verbose_name='описание', blank=True)
    is_active = models.BooleanField(verbose_name='активна', default=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='имя продукта', max_length=128)
    image = models.ImageField(upload_to='product_images', blank=True)
    short_desc = models.CharField(verbose_name='краткое описание продукта', max_length=60, blank=True)
    description = models.TextField(verbose_name='описание продукта', blank=True)
    price = models.DecimalField(verbose_name='цена продукта', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name='количество на складе', default=0)

    def __str__(self):
        return f'{self.name} ({self.category.name})'


class ContactCategory(models.Model):
    name = models.CharField(verbose_name='имя', max_length=64, unique=True)
    description = models.TextField(verbose_name='описание', blank=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    category = models.ForeignKey(ContactCategory, on_delete=models.CASCADE)
    city = models.CharField(verbose_name='город', max_length=128)
    phone_number = models.CharField(verbose_name='телефон', max_length=17)
    email = models.CharField(verbose_name='email', max_length=60, blank=True)
    address = models.TextField(verbose_name='адрес', blank=True)

    def __str__(self):
        return f'{self.city} ({self.category.name})'

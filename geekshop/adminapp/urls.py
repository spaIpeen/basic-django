import adminapp.views as adminapp
from django.urls import path

app_name = 'adminapp'

urlpatterns = [
    path('users/create/', adminapp.UsersCreateView.as_view(), name='user_create'),
    path('users/read/', adminapp.UsersListView.as_view(), name='users'),
    path('users/update/<int:pk>/', adminapp.UsersUpdateView.as_view(), name='user_update'),
    path('users/delete/<int:pk>/', adminapp.UsersDeleteView.as_view(), name='user_delete'),

    path('categories/create/', adminapp.ProductCategoryCreateView.as_view(), name='category_create'),
    path('categories/read/', adminapp.ProductCategoryListView.as_view(), name='categories'),
    path('categories/update/<int:pk>/', adminapp.ProductCategoryUpdateView.as_view(), name='category_update'),
    path('categories/delete/<int:pk>/', adminapp.ProductCategoryDeleteView.as_view(), name='category_delete'),

    path('product/create/category/<int:pk>/', adminapp.product_create, name='product_create'),
    path('product/read/category/<int:pk>/', adminapp.products, name='products'),
    path('product/read/<int:pk>/', adminapp.ProductDetailView.as_view(), name='product_read'),
    path('product/update/<int:pk>/', adminapp.product_update, name='product_update'),
    path('product/delete/<int:pk>/', adminapp.ProductDeleteView.as_view(), name='product_delete'),

    path('orders/read/', adminapp.OrdersReadView.as_view(), name='orders'),
]

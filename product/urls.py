from django.urls import path

from .views import AddProductView, list_product, list_product_wallpaper, list_product_artifact, product_detail, search

app_name = 'products'
urlpatterns = [
    path('new/', AddProductView.as_view(), name='new_product'),
    path('list_product', list_product, name='list_product'),
    path('list_product/wallpaper/', list_product_wallpaper, name='list_product_wallpaper'),
    path('list_product/artifact/', list_product_artifact, name='list_product_artifact'),
    path('search/', search, name='filter_product'),
    path('<pk>/', product_detail, name='product_detail'),
]


# list of namespace urls for templates:
#     products:new_product
#     products:product_list
#     products:detailed_product
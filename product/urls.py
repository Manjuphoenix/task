from django.conf.urls import url
from django.urls import path, include

from .views import AddProductView, ListProductsView, ProductDetail, SearchProduct

app_name = 'products'
urlpatterns = [
    path('new/', AddProductView.as_view(), name='new_product'),
    path('list_product/', ListProductsView.as_view(), name='list_product'),
    path('<pk>/', ProductDetail.as_view(), name='product_detail'),
]


# list of namespace urls for templates:
#     products:new_product
#     products:product_list
#     products:detailed_product
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views.generic import FormView, ListView, CreateView, DetailView
from django.http import request

from .models import Product
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class ProductDetail(DetailView):
    model = Product
    template_name = 'product/product_detail.html'



class AddProductView(LoginRequiredMixin, CreateView):
    model = Product
    template_name = 'product/add_product.html'
    fields = ['title', 'type', 'image', 'description']


class ListProductsView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'product/list_product.html'
    paginate_by = 2

class SearchProduct(ListView):
    model = Product
    # query = """
    # SELECT * FROM `Product` WHERE
    template_name = 'search_result.html'
    context_object_name = 'products'

    def get_queryset(self, **kwargs):
        context = super(SearchProduct, self).get_context_data(**kwargs)
        query_result = self.get_queryset()
        return context

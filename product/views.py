from django.shortcuts import render, get_object_or_404
from django.views.generic import FormView, ListView, CreateView, DetailView
from django.http import request

from .models import Product
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class ProductDetail(DetailView):
    model = Product
    template_name = 'product/product_detail.html'

    # def get_object(self):
    #     id_ = self.kwargs.get("id")
    #     return get_object_or_404(Product, id=id_)


class AddProductView(LoginRequiredMixin, CreateView):
    model = Product
    template_name = 'product/add_product.html'
    fields = ['title', 'type', 'image', 'description']


class ListProductsView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'product/list_product.html'

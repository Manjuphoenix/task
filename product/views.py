from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from .filters import *
from django.core.paginator import Paginator

from rest_framework import viewsets, permissions
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from product.serializers import ProductSerializer

from .models import Product
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

# class ProductDetail(DetailView):
#     model = Product
#     template_name = 'product/product_detail.html'


def product_detail(request, pk):
    context = {}
    context["data"] = Product.objects.get(id = pk)
    return render(request, 'product/product_detail.html', context)


class AddProductView(LoginRequiredMixin, CreateView):
    model = Product
    template_name = 'product/add_product.html'
    fields = ['title', 'type', 'image', 'description']


# class ListProductsView(LoginRequiredMixin, ListView):
#     model = Product
#     template_name = 'product/list_product.html'
#     paginate_by = 2

def list_product(request):
    query_product = Product.objects.all()
    product = Product.objects.all()
    paginator = Paginator(product, 3)
    # The page query string value is fetched with the request.GET.get() function and passed to the paginator.get_page()
    page = request.GET.get('page')
    product = paginator.get_page(page)
    filter = ProductFilter(request.GET, queryset=query_product)
    return render(request, 'product/list_product.html', {'product': product, 'filter': filter})


def list_product_wallpaper(request):
    product = Product.objects.filter(type="Wallpaper")
    filter = ProductFilter(request.GET, queryset=product)
    return render(request, 'product/list_product.html', {'filter': filter})


def list_product_artifact(request):
    product = Product.objects.filter(type="Artifact")
    filter = ProductFilter(request.GET, queryset=product)
    return render(request, 'product/list_product.html', {'filter': filter})


def search(request):
    objects = Product.objects.all()
    filter = ProductFilter(request.GET, queryset=objects)
    return render(request, 'product/list_product.html', {'filter': filter})


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

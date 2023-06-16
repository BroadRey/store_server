from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from products.models import Product, ProductCategory


def index(request: HttpRequest) -> HttpResponse:
    context = {
        'title': 'Test Title',
    }

    return render(request, 'products/index.html', context=context)


def products(request: HttpRequest) -> HttpResponse:
    context = {
        'title': 'Store - Каталог',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all()
    }

    return render(request, 'products/products.html', context=context)

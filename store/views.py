from django.shortcuts import render, get_object_or_404

from category.models import Category
from store.models import Product


# Create your views here.


def store(request, category_slug=None):
    category = None
    products = None
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category, is_available=True)
    else:
        products = Product.objects.all().filter(is_available=True)
    product_count = products.count()
    context = {
        'products': products,
        'product_count': product_count
    }
    return render(request, 'store/store.html', context)


def product_detail(request, category_slug=None, product_slug=None):
    try:
        product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    except Exception as exc:
        raise exc
    context = {
        'product': product
    }
    return render(request, 'store/product_detail.html', context)

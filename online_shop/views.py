from django.shortcuts import render

from online_shop.models import Product, Category


def products_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'online_shop/home.html', context)

def products_all_view(request):
    products = Product.objects.get(pk=id)
    context = {'products': products}
    return render(request, 'online_shop/detail.html', context)

def category(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'online_shop/home.html', context)

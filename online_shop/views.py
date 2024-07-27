from django.shortcuts import render

from online_shop.models import Product


def products_list(request):
    return render(request, 'online_shop/home.html')

def products_all_view(request):
    products = Product.objects.all()
    return render(request, 'online_shop/detail.html')


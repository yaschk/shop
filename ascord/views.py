from django.shortcuts import render
from ascord.models import *

def index(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_cans = products_images.filter(product__category__id=1)
    products_images_markers = products_images.filter(product__category__id=2)
    products_images_3 = products_images.filter(product__category__id=3)
    products_images_4 = products_images.filter(product__category__id=4)
    # last_products = products_images.order_by("-id")[0:3]

    return render(request, 'landing/index.html', locals())


def product(request, product_id):
    product = Product.objects.get(id=product_id)

    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    print(request.session.session_key)

    return render(request, 'landing/product.html', locals())

def info (request):

    return render(request, 'landing/info.html', locals())

def contacs (request):

    return render(request, 'landing/contacts.html', locals())

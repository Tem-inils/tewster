from django.shortcuts import render
from .models import MainProduct, ProductImage


# Create your views here.
def index(request):
    product = MainProduct.objects.all()
    # for i in product:
    #     print(i.title)
    if product:
        return render(request, 'mainapp/index.html', {"product": product})
    else:
        return render(request, 'mainapp/index.html')


def test(request):
    product = MainProduct.objects.all()
    print(product)
    # for i in product:
    #     print(i.title)
    if product:
        return render(request, 'mainapp/test.html', {"product": product})
    else:
        return render(request, 'mainapp/test.html')


def news(request):
    return render(request, 'mainapp/news.html')


def photo(request):
    return render(request, 'mainapp/photo.html')

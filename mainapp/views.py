from django.shortcuts import render
from .models import MainProduct, ProductImage


# Create your views here.
def index(request):
    product1 = MainProduct.objects.filter(category="Ex-Proof ME").all()
    product2 = MainProduct.objects.filter(category="QM 1000V").all()
    context = {
        "category1": product1,
        "category2": product2
    }
    return render(request, 'mainapp/index.html', context)


def test(request):
    product = MainProduct.objects.all()
    if product:
        return render(request, 'mainapp/test.html', {"product": product})
    else:
        return render(request, 'mainapp/test.html')


def news(request):
    return render(request, 'mainapp/news.html')


def photo(request):
    return render(request, 'mainapp/photo.html')

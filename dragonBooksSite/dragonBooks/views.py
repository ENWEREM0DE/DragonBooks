from django.core import paginator
from django.shortcuts import render
from .models import Products
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    return render(request, 'dragonBooks/index.html')

def checkout(request):
    return render(request, 'dragonBooks/checkout.html')


def shop(request):
    product_objects = Products.objects.all()
    return render(request, 'dragonBooks/shop.html', {'product_objects':product_objects} )

def about(request):
    return render(request, 'dragonBooks/about.html')

def contact(request):
    return render(request, 'dragonBooks/contact.html')

def cart(request):
    return render(request, 'dragonBooks/cart.html')

def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        books = Products.objects.filter(name__contains=searched)
        return render(request, 'dragonBooks/search.html', {'searched':searched, 'books':books})
    
    else:
        return render(request, 'dragonBooks/search.html', {})

def codeSearch(request):
    if request.method == "POST":
        codeSearched = request.POST['codeSearched']
        books = Products.objects.filter(classCode__contains=codeSearched)
        return render(request, 'dragonBooks/codeSearch.html', {'codeSearched':codeSearched, 'books':books})
    else:
        return render(request, 'dragonBooks/codeSearch.html', {})



def searchCode(request):
    return render(request, 'dragonBooks/searchCode.html', {} )

def single(request,id):
    product_object = Products.objects.get(id=id)
    return render(request, 'dragonBooks/singlebook.html', {'product_object':product_object})

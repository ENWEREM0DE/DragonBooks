from django.core import paginator
from django.shortcuts import render
from django.http import JsonResponse
from .models import *
import json
from django.core.paginator import Paginator
# Create your views here.


def index(request):
    return render(request, 'dragonBooks/index.html')


def checkout(request):
    return render(request, 'dragonBooks/checkout.html')


def shop(request):
    product_objects = Products.objects.all()
    return render(request, 'dragonBooks/shop.html', {'product_objects': product_objects})


def about(request):
    return render(request, 'dragonBooks/about.html')


def contact(request):
    return render(request, 'dragonBooks/contact.html')


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
    context = {'items': items, 'order': order}
    return render(request, 'dragonBooks/cart.html', context)


def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        books = Products.objects.filter(name__contains=searched)
        return render(request, 'dragonBooks/search.html', {'searched': searched, 'books': books})

    else:
        return render(request, 'dragonBooks/search.html', {})


def codeSearch(request):
    if request.method == "POST":
        codeSearched = request.POST['codeSearched']
        books = Products.objects.filter(classCode__contains=codeSearched)
        return render(request, 'dragonBooks/codeSearch.html', {'codeSearched': codeSearched, 'books': books})
    else:
        return render(request, 'dragonBooks/codeSearch.html', {})


def searchCode(request):
    return render(request, 'dragonBooks/searchCode.html', {})


def single(request, id):
    product_object = Products.objects.get(id=id)
    return render(request, 'dragonBooks/singlebook.html', {'product_object': product_object})


def forthepress(request):
    return render(request, 'dragonBooks/forthepress.html', {})


def booksellers(request):
    return render(request, 'dragonBooks/booksellers.html', {})


def mediamentions(request):
    return render(request, 'dragonBooks/mediamentions.html', {})


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('action:', action)
    print('productId:', productId)

    customer = request.user.customer
    product = Products.objects.get(id=productId)
    order, created = Order.objects.get_or_create(
        customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(
        order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)

    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse('Item was added', safe=False)

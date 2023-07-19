from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect


def index(request):
    return HttpResponse("<h2>Главная</h2>")


def about(request):
    return HttpResponse("<h2>О сайте</h2>")


def contact(request):
    # return HttpResponse("<h2>Контакты</h2>")
    return HttpResponseRedirect("/about")


def details(request):
    return HttpResponsePermanentRedirect("/")


def products(request, productid=1):
    output = "<h2>Product # {}</h2".format(productid)
    return HttpResponse(output)


def users(request, id=1, name="Valera"):
    output = "<h2>User</h2><h3>id: {0}<br/>name: {1}</h3>".format(id, name)
    return HttpResponse(output)

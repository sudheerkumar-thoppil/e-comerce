from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("you are in product page")

# Create your views here.

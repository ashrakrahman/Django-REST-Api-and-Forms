from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *

def product (request):
    template = loader.get_template('product.html')
    context = {
        'products': Product.objects.all()
    }
    return HttpResponse(template.render(context,request))

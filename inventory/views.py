from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Item
def Controlroom(request):
    Item_list = Item.objects.all()
    template = loader.get_template("inventory/Controlroom.html")
    context = {
        "Item_list": Item_list,
    }
    return HttpResponse(template.render(context,request))

def Itemdetails(request, item_id):
    
    template = loader.get_template("inventory/Itemdetails.html")
    context = {
        "Item": Item.objects.get(id = item_id),
    }
    return HttpResponse(template.render(context,request))
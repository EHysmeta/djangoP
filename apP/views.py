from django.shortcuts import render
from .models import *
# Create your views here.
def home (request):
    items = Item.objects.all()    
    categorys = category.objects.all()
    contex = {"items_value":items,"categorys_value":categorys}
    return render(request,'home.html',contex)


def about (request):
    items = Item.objects.all()
    contex = {"items_value":items}
    return render(request,'about.html',contex)




    
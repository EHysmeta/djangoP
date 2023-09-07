from django.shortcuts import render
from .models import *
# Create your views here.
def home (request):
    items = Item.objects.all()
    contex = {"items_value":items}
    return render(request,'home.html',contex)


    
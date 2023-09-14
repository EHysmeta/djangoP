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
    
    
def contact (request):
    # if request.method =="POST":
    #     emri = request.POST["emri"]
    #     mbiemri = request.POST["mbiemri"]
    #     email = request.POST["email"]
    #     sms = request.POST["sms"]
    
    #     Contact(
    #         contact_name = emri,
    #         contact_surname = mbiemri,
    #         contact_email = email,
    #         contact_sms = sms,
    #         ).save()
    return render(request, 'contacts.html')

def itemdetail (request, id):
    item_detail = Item.objects.get(pk=id)
    contex = {"item_detail":item_detail}
    return render(request, "itemdetail.html", contex)


def Category (request, id):
    category_ = category.objects.get(pk=id)
    category_items = Item.objects.filter(item_category=category_)
    contex = {"category":category_, 'category_items':category_items}
    return render(request, "category.html", contex)




    
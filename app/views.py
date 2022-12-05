from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from app.models import ProductTable
from django.urls import reverse
from django.template import loader
from django.template.loader import get_template



# Create your views here.
def base(request):
    return render(request,"base.html")

def data(request):
    product = ProductTable.objects.all().values()
    context = {
        'product':product,
    }
    return render(request,"data.html",context)

def addproduct(request):
    template = loader.get_template('addproduct.html')
    return HttpResponse(template.render({},request))

def addrecord(request):
    name = request.POST['enter name'] 
    quantity = request.POST['quantity']
    price = request.POST['price']  
    product = ProductTable(name = name,quantity=quantity,price=price)
    product.save()
    return HttpResponseRedirect(reverse('datapage'))  

def delete(request,pid):
    product = ProductTable.objects.get(id=pid)
    product.delete()
    return HttpResponseRedirect(reverse('datapage'))

def update(request, pid):   
    product = ProductTable.objects.get(id=pid)
    context = {
        'product':product,
    }
    return render(request,"update.html",context)


def update_product(request, pid):
    name = request.POST['enter name'] 
    quantity = request.POST['quantity']
    price = request.POST['price']  
    product = ProductTable.objects.get(id=pid)
    product.name = name
    product.quantity = quantity
    product.price = price
    product.save()
    return HttpResponseRedirect(reverse('datapage'))  

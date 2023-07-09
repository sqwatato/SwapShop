from django.shortcuts import redirect, render
from django.http import JsonResponse
# from .forms import ProblemForm
from .models import Clothing, User, Trade
import requests
import json
from pprint import pprint
# from dotenv import load_dotenv
# import os
# # import openai
# load_dotenv()


# Create your views here.

def index(request):
    return render(request, 'pages/index.html', {
        'nums': (User.objects.count(), Clothing.objects.count(), Trade.objects.count()),
    })
        
def trades(request):
    tmp =  Clothing.objects.all()
    size = len(tmp)
    # Split into groups of 3
    clothing = []
    for i in range(size//3+1):
        tmp2 = []
        for j in range(3):
            if i*3+j < size:
                tmp2.append(tmp[i*3+j])
        clothing.append(tmp2)

    categories = [
        Clothing.COLOR_CHOICES,
        Clothing.SIZE_CHOICES,
        Clothing.CLOTHING_TYPE_CHOICES
    ]
    
    return render(request, 'pages/trades.html', {
        'clothing': clothing,
        'size' : size,
        'categories' : categories
    })

def score(object, color, size, cType, search):
    size2 = {
        'XS' : 0,
        'S' : 1,
        'M' : 2,
        'L' : 3,
        'XL' : 4,
    }
    s = 0
    if object.color == color:
        s += 7
    if size != 'None':
        if size2[object.size] == size2[size]:
            s += 5
        elif size2[object.size] == size2[size]+1 or size2[object.size] == size2[size]-1:
            s += 3
    if object.cType == cType:
        s += 10
    if search.lower().strip() in object.title.lower().strip():
        s += 10
    
    for i in (color, size, cType, search):
        if i == 'None':
            s += 10
    
    return s
        
        

def filter(request, color, size, cType, search):
    tmp = Clothing.objects.all()
    clothing2 = sorted(tmp, reverse=True, key=lambda x: score(x, color, size, cType, search))
    clothing2 = [ i for i in clothing2 if score(i, color, size, cType, search) > 20]
    if color == "None":
        color = None
    if size == "None":
        size = None
    if cType == "None":
        cType = None
    if search == "None":
        search = None
    size = len(clothing2)
    
    clothing = []
    for i in range(size//3+1):
        tmp2 = []
        for j in range(3):
            if i*3+j < size:
                tmp2.append(clothing2[i*3+j])
        clothing.append(tmp2)

    categories = [
        Clothing.COLOR_CHOICES,
        Clothing.SIZE_CHOICES,
        Clothing.CLOTHING_TYPE_CHOICES
    ]    
    
    return render(request, 'pages/filter.html', {
        'clothing': clothing,
        'size' : size,
        'categories' : categories
    })
    


def create(request):
    if request.user.is_authenticated:
        categories = [
            Clothing.COLOR_CHOICES,
            Clothing.SIZE_CHOICES,
            Clothing.CLOTHING_TYPE_CHOICES
        ] 
        if request.method == 'POST':
            user = request.user
            title = request.POST['title']
            color = request.POST['color']
            size = request.POST['size']
            cType = request.POST['cType']
            image = request.FILES['image']
            clothing = Clothing(user=user, title=title, color=color, size=size, cType=cType, image=image)
            clothing.save()
            return redirect('trades')
        else:
            return render(request, 'pages/create.html', {
                'categories' : categories
            })
    return redirect('login')

def listing(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            id1 = request.POST['id1']
            id2 = request.POST['id2']
            trade = Trade(user1=request.user, user2=Clothing.objects.get(id=id1).user)
            trade.save()
            c1 = Clothing.objects.get(id=id1)
            c2 = Clothing.objects.get(id=id2)
            c1.trade = trade
            c1.save()
            c2.trade = trade
            c2.save()
            return redirect('trades')
        else:
            return render(request, 'pages/listing.html', {
                "listing" : Clothing.objects.get(id=id),
                "other" : Clothing.objects.filter(user=request.user)
            })
    return render(request, 'pages/listing.html', {
        "listing" : Clothing.objects.get(id=id),
        "other" : Clothing.objects.filter(user=request.user)
    })
    
def opentrades(request):
    trades = []
    for t in Trade.objects.all():
        # u1 = t.user1
        # u2 = t.user2
        tmp = Clothing.objects.filter(trade=t)

        trades.append([tmp[0], tmp[1]])
    return render(request, 'pages/opentrades.html', {
        "trades" : trades
    })
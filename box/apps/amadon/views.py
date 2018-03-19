# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    # intialize the inventory
    if 'inventory' not in request.session:
        inventory = []
        inventory.append({'name':'Dojo Tshirt', 'price':19.99 })
        inventory.append({'name':"Dojo Sweater", 'price':29.99})
        inventory.append({'name':"Dojo Cup", 'price':4.99})
        inventory.append({'name':"Algorithm Book", 'price':49.99})
        inventory.append({'name':"Ninja Pants", 'price':12.49})
        request.session['inventory'] = inventory
    
    # initialize the running total
    if 'total' not in request.session:
        request.session['total'] = 0
    
    #initialize the running item count
    if 'count' not in request.session:
        request.session['count'] = 0
        
    # initialize the charge 
    request.session['charge'] = 0
    
    return render (request, 'amadon/index.html')

def process(request):
    # accept POST data to vars
    quantity = request.POST['quantity']
    price = request.POST['price']
    
    # assign values to session
    request.session['quantity'] = quantity
    request.session['price'] = price
    
    # process data for tier 2 feedback
    request.session['count'] += int(quantity)
    charge = float(price) * int(quantity)
    request.session['charge'] = charge
    request.session['total'] += charge

    return redirect('/checkout')

def display(request):
    # request.session.flush()  ##used this session clear for testing
    return render(request, 'amadon/checkout.html')

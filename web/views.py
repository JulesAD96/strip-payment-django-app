from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse

import stripe
stripe.api_key = "sk_"


def index(request):
	return render(request, 'web/index.html')


def charge(request):
    
    if request.method == "POST":
        amount = int(request.POST["amount"])
        customer = stripe.Customer.create(
            email = request.POST["email"],
            name = request.POST["name"],
            source = request.POST["stripeToken"]
        )
        
        charge = stripe.Charge.create(
            customer=customer,
            amount=amount*100,
            currency="usd",
            description="Donnation",
        )
    return redirect(reverse("success", args=[amount]))


def successMsg(request, args):
	amount = args
	return render(request, 'web/success.html', {'amount':amount})

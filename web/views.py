from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse

import stripe
stripe.api_key = "sk_test_51I5qyyHGmSftft1XT4J34kJxNQD97hn0EO0bQ3qHgafBo2DSRv0PE61nh8ZIbdJBLkRQL3g41LORBCis3tphxhfd00QvgOFnna"


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
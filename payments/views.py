from django.shortcuts import render,redirect
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.conf import settings 
from django.core import serializers
import stripe
from bs4 import BeautifulSoup
import requests
import os
from django.views.decorators.csrf import csrf_exempt
from . import models
from .models import GetAmount
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
import json
from data.models import Club
from posts import models 
from posts.models import Posts
    
#@require_POST()
@csrf_exempt
def scrape_amount(request):
    if request.method=='POST':
        if "mate" in request.POST:
            x = request.POST.get("mate")#request.POST.get('stripe_val') #sets value attribut equal to the server side value
            number = GetAmount() #creates an object
            number.value = x #request.POST.get('stripe_val') #sets value attribut equal to the server side value
            number.save() #saves object down to be used later

            stripe.api_key = 'sk_test_iBjWZaOdbwtP44prkHZeD2Jy002SrATNFK'
            intent = stripe.PaymentIntent.create(
            amount= x,
            currency='gbp',
            metadata={
                'integration_check': 'accept_a_payment'
                }
            )
            context = {
                "secret": intent.client_secret,
                "feed"  : Posts.objects.all(),
                }

            secret = intent.client_secret
            return HttpResponse(secret)

        
        else:
            y = request.POST
            user = y["name"] 
            donation = y["donation"]
            team = y["team"].strip()
            message = Posts()
            message.name = user
            message.value = donation
            message.team = Club.objects.get(team=team)
            message.save()
            return JsonResponse({'name': message.name, 'value': message.value, 'team': message.team.team})

    else :
        return render(request, 'payments/home.html')


@csrf_exempt    
def amountview(request):
    return render(request, "payments/stripe.html")


class StripeView(ListView):
    template_name ="payments/prestripe.html"
    model = Posts
    context_object_name = 'posts'
    
    def get_context_data(self, **kwargs): #**kwargs is basically a dictionary of any key and value pairs 
        context = super().get_context_data(**kwargs) #super() gets the context from the parent class ie StipeViews
        context['key'] = 'pk_test_sMuUdXvGiOEvFLSOAlPFFLaY008Afnd6pY' #if context contains 'key' in dictionary somwhere set the value to that publishable key
        return context #returns the value for 'key' IN THE TEMPLATE in {{key}}

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(StripeView, self).dispatch(request, *args, **kwargs)

    
class HomePageView(TemplateView):
    template_name = "payments/home.html"
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['key'] = 'pk_test_sMuUdXvGiOEvFLSOAlPFFLaY008Afnd6pY'
        return context

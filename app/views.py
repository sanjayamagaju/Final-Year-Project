from ast import If
from dataclasses import fields
from multiprocessing import Manager, context, managers
from pyexpat import model
from re import template
import re
from tkinter import TOP
from tokenize import Name
from typing_extensions import Self
from urllib import request
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from matplotlib.cbook import maxdict
from matplotlib.pyplot import get
from psutil import users
from django.contrib.auth.models import User
from pyparsing import col
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages
from .models import Gallery, LeaderBoard, OtherCampaign, FuturePurpose
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.db.models import Q
import requests, json
from django.http import JsonResponse



# Create your views here.
@login_required(login_url='login')
# homepage
def home(request):
    trendings = OtherCampaign.objects.filter().order_by('-Donation_count')[:5]
    leaderboard = LeaderBoard.objects.filter().order_by('-donation_amt')[:8]
    context = {
        'nav_bar' : 'home',
        'leaderboards' : leaderboard,
        'trendings' : trendings,
    }
    return render(request,'home.html', context)

# howitworks page
def howitworks(request):
    context = {
        'nav_bar' : 'howitworks'
    }
    return render(request, 'howitworks.html', context)

# gallery page
def gallery(request):
    gallery_context = {
        'galleryimg' : Gallery.objects.all(),
        'nav_bar' : 'gallery'
    }
    return render(request, 'gallery.html', gallery_context)


# othercampaign page
def othercampaign(request):
    context = {
        'other_campaigns' : OtherCampaign.objects.all(),
    }
    return render(request, 'othercampaign.html', context)

# othercampaign page
def future_purpose(request):
    context = {
        
    }
    
    return render(request, 'future_purpose.html', context)

# khalti request view
def khaltirequest(request, id):
    context = {
        'khalti_api' : get_object_or_404(OtherCampaign, pk=id)
    }
    return render(request, 'khaltirequest.html', context)

def khaltiverify(request, id):
    token = request.GET.get("token")
    amount = request.GET.get("amount")
    collected = request.GET.get("collected")
    donation_count = request.GET.get("donation_counter")
    campaign_id = request.GET.get("campaign_id")
    campaign_name = request.GET.get("campaign_name")
    
    url = "https://khalti.com/api/v2/payment/verify/"
    payload = {
        "token": token,
        "amount": amount,
    }
    headers = {
        "Authorization": "Key test_secret_key_ab4f4a7082cc41f6af3231fb36c82b95"
    }

    response = requests.post(url, payload, headers = headers)
    resp_dict = response.json()
    print(resp_dict)
    user_name = resp_dict.get("user")
    user = user_name['name']
    # print(user)
    date_donate = resp_dict.get("created_on")
    # product_identity = resp_dict.get("product_identity")
    if resp_dict.get("idx"):
        success = True

        data = LeaderBoard(
            token = token,
            donor = user,
            donation_amt = amount,
            camp_detail = campaign_name,
            date_donation = date_donate
        )
        data.save()

        # if product_identity == campaign_id:
        collected = int(collected)
        amount = int(amount)
        dc = int(donation_count)
        dc = dc + 1
        collected += amount/100
        
        
        OtherCampaign.objects.filter(id=campaign_id).update(Amount=amount, Collected=collected, Donation_count=dc)

    else: 
        success = False
    succ = {
        'success' : success
    }

    return JsonResponse(succ)

# khalti request for future purpose
def future_khalti(request):
    context = {
        
    }
    return render(request, 'future_khalti.html', context)

def khaltiverify_future(request):
    token = request.GET.get("token")
    amount = request.GET.get("amount")

    url = "https://khalti.com/api/v2/payment/verify/"
    payload = {
        "token": token,
        "amount": amount
    }
    headers = {
        "Authorization": "Key test_secret_key_48e4a75d471b420093957150969b830f"
    }

    response2 = requests.post(url, payload, headers = headers)
    resp_dict2 = response2.json()
    if resp_dict2.get("idx"):
        success = True
        data2 = FuturePurpose(
            amount = amount,
            token = token
        )
        data2.save()
    else: 
        success = False
    succ2 = {
        'success' : success
    }

    return JsonResponse(succ2)



# detail page
def detail(request, id):
    context = {
        'camp_detail' : get_object_or_404(OtherCampaign, pk=id),
    }
    return render(request, 'detail.html', context)


# registerpage
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was successfully created for ' + user)

                return redirect('login')

        context = {'form':form}
        return render(request, 'register.html', context)


# loginpage
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Incorrect username or password')

        context = {}
        return render(request, 'login.html', context)

# logout 
def logoutUser(request):
    logout(request)
    return redirect('login')


# CRUD from user side
# create campaign
class CampaignCreateView(CreateView):
    model = OtherCampaign
    template_name = 'create.html'
    fields = ['Name', 'Image', 'Target', 'Collected', 'Info']
    success_url = '/othercampaign/'

    def form_valid(self, form):
        instance = form.save(commit = False)
        instance.manager = self.request.user
        instance.save()
        return redirect('campaign')

# update campaign
class CampaignUpdateView(UpdateView):
    model = OtherCampaign
    template_name = 'update.html'
    fields = ['Name', 'Image', 'Target', 'Collected', 'Info']

    def form_valid(self, form):
        instance = form.save()
        return redirect('detail', instance.pk)

    # user control
    def get_queryset(self):
        updates = super().get_queryset()
        return updates.filter(manager = self.request.user)

# delete campaign
class CampaignDeleteView(DeleteView):
    model = OtherCampaign
    template_name = 'delete.html'
    success_url = '/othercampaign/'

    # user control
    def get_queryset(self):
        updates = super().get_queryset()
        return updates.filter(manager = self.request.user)
    

# search page
def search(request):
    if request.GET:
        search_term = request.GET['search_term']
        search_results = OtherCampaign.objects.filter(
            Q(Name__icontains=search_term) |
            Q(Info__icontains=search_term)

        )
        context = {
            'search_term' : search_term,
            'other_campaigns' : search_results
        }
        return render(request, 'search.html', context)
    else:
        return redirect('home')

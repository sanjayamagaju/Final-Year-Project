from dataclasses import fields
from multiprocessing import context
from pyexpat import model
from re import template
import re
from urllib import request
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Campaign, Gallery
from .models import OtherCampaign
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.db.models import Q


# Create your views here.
@login_required(login_url='login')
# homepage
def home(request):
    context = {
        'campaigns' : Campaign.objects.all()
    }
    return render(request,'home.html', context)


# gallery page
def gallery(request):
    gallery_context = {
        'galleryimg' : Gallery.objects.all()
    }
    return render(request, 'gallery.html', gallery_context)

# othercampaign page
def othercampaign(request):
    context = {
        'other_campaigns' : OtherCampaign.objects.all()
    }
    return render(request, 'othercampaign.html', context)
    

# detail page
def detail(request, id):
    context = {
        'camp_detail' : get_object_or_404(OtherCampaign, pk=id) 
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
            Q(Info__iexact=search_term)

        )
        context = {
            'search_term' : search_term,
            'other_campaigns' : search_results
        }
        return render(request, 'search.html', context)
    else:
        return redirect('home')



# khalti payment gateway
import requests

url = "https://khalti.com/api/v2/payment/verify/"
payload = {
  "token": "QUao9cqFzxPgvWJNi9aKac",
  "amount": 1000
}
headers = {
  "Authorization": "Key test_secret_key_ab4f4a7082cc41f6af3231fb36c82b95"
}

response = requests.post(url, payload, headers = headers)
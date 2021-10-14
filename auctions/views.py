from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import *


def index(request):
    return render(request, "auctions/index.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        usr = authenticate(request, username=username, password=password)

        if usr is not None:
            login(request, usr)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "User or Password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Error. Passwords are different."
            })
        try:
            usr = User.objects.create_user(username, email, password)
            usr.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Error. User exists."
            })
        login(request,usr)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

@login_required
def watchlist_view(request):
    return render(request, "auctions/watchlist.html")

@login_required
def comment_view(request):   
    return render(request, "auctions/comment.html")

@login_required
def active_listings_view(request):
    return render(request, "auctions/active_listings.html")

@login_required
def create_listings_view(request):
    return render(request, "auctions/create_listings.html",{
        "categories": dicCategorie,
        })
@login_required
def submit(request):
    if request.method=="POST":
        

@login_required
def listings_view(request):
    return render(request, "auctions/listings.html")

@login_required
def categories_view(request):
    return render(request, 'auctions/categories.html', {
        "categories": dicCategorie,
    })
    
@login_required
def category_listings(request,category):
    listings = Listing.objects.filter(category__in = category[0])
    cat = dict(dicCategorie)
    return render(request, 'auctions/categorie.html', {
        "listings": listings,
        "category": cat[category]
    })

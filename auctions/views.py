from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import *
from .forms import *


def index(request):
    return render(request, "auctions/index.html", {"listings": listing.objects.all()})


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


@login_required
def categories_view(request):
    return render(request, 'auctions/categories.html', {
        "categories": dicCategorie,
    })


@login_required
def category_listings(request, category):
    listings = Listing.objects.filter(category__in=category[0])
    cat = dict(dicCategorie)
    return render(request, 'auctions/categorie.html', {
        "listings": listings,
        "category": cat[category]
    })


@login_required
def watchlist_view(request):
    return render(request, "auctions/watchlist.html")


@login_required
def comment_view(request):
    return render(request, "auctions/comment.html")


@login_required
def create_listings_view(request):
    if request.method == "POST":
        user = User.objects.get(username=request.user)
        form = listing_form(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.owner = user
            listing.save()
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/create_listings.html", {"form": form, "categories": dicCategorie})
    else:
        return render(request, "auctions/create_listings.html", {"form": listing_form(), "categories": dicCategorie})


@login_required
def submit(request):
    if request.method == "POST":
        return()


@login_required
def active_listings_view(request):
    return render(request, "auctions/active_listings.html")


@login_required
def listings_view(request, idListing):
    listing = Listing.objects.get(pk=idListing)
    if request.method == "POST":
        user = User.objects.get(username=request.user)
        if request.POST.get("button") == "Watchlist":
            if not user.watchlist.filter(listing=listing):
                watchlist = watchlist()
                watchlist.user = user
                watchlist.listing = listing
                watchlist.save()
            else:
                user.watchlist.filter(listing=listing).delete()
            return HttpResponseRedirect(reverse('listing', args=(listing.id,)))
        if not listing.closed:
            if request.POST.get("button") == "Close":
                listing.closed = True
                listing.save()
            else:
                price = float(request.POST["price"])
                bids = listing.bids.all()
                if user.username != listing.owner.username:  # only let those who dont own the listing be able to bid
                    if price <= listing.price:
                        return render(request, "auctions/listing.html", {
                            "listing": listing,
                            "form": BidForm(),
                            "message": "Error! Invalid bid amount!"
                        })
                    form = BidForm(request.POST)
                    if form.is_valid():
                        # clean up this
                        bid = form.save(commit=False)
                        bid.user = user
                        bid.save()
                        listing.bids.add(bid)
                        listing.price = price
                        listing.save()
                    else:
                        return render(request, 'auctions/listing.html', {
                            "form": form
                        })
        return HttpResponseRedirect(reverse('listing', args=(listing.id,)))
    else:
        return render(request, "auctions/listing.html", {
            "listing": listing,
            "form": BidForm(),
            "message": ""
        })


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
        login(request, usr)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

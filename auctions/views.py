from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import *
from .models import *


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
    listings = listing.objects.filter(category__in=category[0])
    cat = dict(dicCategorie)
    return render(request, 'auctions/specific.html', {
        "listings": listings,
        "category": cat[category]
    })


@login_required
def watchlist_view(request):
    user = User.objects.get(username=request.user)
    return render(request, "auctions/watchlist.html", {
        "watchlist": user.watchlist.all()
    })


@login_required
def comment_view(request, id):
    user = User.objects.get(username=request.user)
    listing = listing.objects.get(pk=id)
    if request.method == "POST":
        form = comment_form(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = user
            comment.save()
            listing.comments.add(comment)
            listing.save()

            return HttpResponseRedirect(reverse('listing', args=(listing.id,)))
        else:
            return render(request, "auctions/comment.html", {
                "form": form,
                "listing_id": listing.id,
            })
    else:
        return render(request, "auctions/comment.html", {
            "form": comment_form(),
            "listing_id": listing.id
        })


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
def listings_view(request, id):
    Listing = listing.objects.get(pk=id)
    if request.method == "POST":
        user = User.objects.get(username=request.user)
        if request.POST.get("button") == "Watchlist":
            if not user.watchlist.filter(listing=Listing):
                watchlist = watchlist()
                watchlist.user = user
                watchlist.listing = Listing
                watchlist.save()
            else:
                user.watchlist.filter(listing=Listing).delete()
            return HttpResponseRedirect(reverse('listing', args=(Listing.id,)))
        if not Listing.closed:
            if request.POST.get("button") == "Close":
                Listing.closed = True
                Listing.save()
            else:
                price = float(request.POST["price"])
                bid = Listing.bid.all()
                if user.username != Listing.owner.username:  # only let those who dont own the listing be able to bid
                    if price <= Listing.price:
                        return render(request, "auctions/listing.html", {
                            "listing": Listing,
                            "form": bid_form(),
                            "message": "Error! Invalid bid amount!"
                        })
                    form = bid_form(request.POST)
                    if form.is_valid():
                        # clean up this
                        bid = form.save(commit=False)
                        bid.user = user
                        bid.save()
                        Listing.bid.add(bid)
                        Listing.price = price
                        Listing.save()
                    else:
                        return render(request, 'auctions/listing.html', {
                            "form": form
                        })
        return HttpResponseRedirect(reverse('listing', args=(Listing.id,)))
    else:
        return render(request, "auctions/listing.html", {
            "listing": Listing,
            "form": bid_form(),
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

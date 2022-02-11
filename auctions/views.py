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
        username_ = request.POST["username"]
        password_ = request.POST["password"]
        usr_ = authenticate(request, username=username_, password=password_)
        if usr_ is not None:
            login(request, usr_)
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
def add_category_view(request,category):
    category_ = category
    #listings_ = listing.objects.filter(category__in = category_[0])
    listings_ = listing.objects.filter(category=category_)
    cat_ = dict(dicCategorie)
    return render(request, 'auctions/categorie.html', {
        "listings": listings_,
        "category": cat_[category_]
    })


@login_required
def watchlist_view(request):
    user = User.objects.get(username=request.user)
    return render(request, "auctions/watchlist.html", {
        "watchlist": user.watchlist.all()
    })


@login_required
def add_watchlist_view(request, id):
    user_ = User.objects.get(username=request.user)
    listing_ = listing.objects.get(pk=id)
    if request.POST.get("button") == "Watchlist":
        watchlist_ = watchlist()
        watchlist_.user = user_
        watchlist_.listing = listing_
        watchlist_.save()
        # return HttpResponseRedirect(reverse('listing', args=(listing_.id,)))
        return render(request, "auctions/listing.html", {
            "listing": listing_,
            "message": "Succesfully added to my Watchlist."
        })
    if request.POST.get("button") == "RWatchlist":
        user_.watchlist.filter(listing=listing_).delete()
        return render(request, "auctions/listing.html", {
            "listing": listing_,
            "message": "Succesfully removed  to my Watchlist."
        })


@login_required
def create_listings_view(request):
    if request.method == "POST":
        user_ = User.objects.get(username=request.user)
        form_ = listing_form(request.POST, request.FILES)
        print(form_)
        if form_.is_valid():
            listing = form_.save(commit=False)
            listing.owner = user_
            listing.save()
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/create_listings.html", {"form": form_, "categories": dicCategorie})
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
    listing_ = listing.objects.get(pk=id)
    if request.method == "POST":
        user = User.objects.get(username=request.user)
        if request.POST.get("button") == "Watchlist":
            if not user.watchlist.filter(listing=listing_):
                watchlist = watchlist()
                watchlist.user = user
                watchlist.listing = listing_
                watchlist.save()
            else:
                user.watchlist.filter(listing=listing_).delete()
            return HttpResponseRedirect(reverse('listing', args=(listing_.id,)))
        if not listing_.closed:
            if request.POST.get("button") == "Close":
                listing_.closed = True
                listing_.save()
            else:
                bid = listing_.bid.all()
                if user.username != listing_.owner.username:  # no es el dueno
                    if price <= listing_.price:
                        return render(request, "auctions/listing.html", {
                            "listing": listing_,
                            "form": bid_form(),
                            "message": "Your bid has a wrong amount."
                        })
                    form_ = bid_form(request.POST)
                    if form_.is_valid():
                        # clean up this
                        bid_ = form_.save(commit=False)
                        bid_.user = user
                        bid_.save()
                        listing_.bid.add(bid_)
                        listing_.price = price
                        listing_.save()
                    else:
                        return render(request, 'auctions/listing.html', {
                            "form": form
                        })
                else:  # es el dueno
                    return render(request, "auctions/listing.html", {
                        "listing": listing_,
                        "form": bid_form(),
                        "message": "Owners cannot make bids!"
                    })

        return HttpResponseRedirect(reverse('listing', args=(listing_.id,)))
    else:
        return render(request, "auctions/listing.html", {
            "listing": listing_,
            "form": bid_form(),
            "message": ""
        })


def comment_view(request, id):
    user_ = User.objects.get(username=request.user)
    listing_ = listing.objects.get(pk=id)
    if request.method == "POST":
        form_ = comment_form(request.POST)
        if form_.is_valid():
            comment_ = form_.save(commit=False)
            comment_.user = user_
            comment_.save()
            listing_.comments.add(comment_)
            listing_.save()

            return HttpResponseRedirect(reverse('listing', args=(listing_.id,)))
        else:
            return render(request, "auctions/comment.html", {
                "form": form_,
                "listing_id": listing_.id,
            })
    else:
        return render(request, "auctions/comment.html", {
            "form": comment_form(),
            "listing_id": listing_.id
        })


def register_view(request):
    if request.method == "POST":
        user_ = request.POST["username"]
        password_ = request.POST["password"]
        email_ = request.POST["email"]
        confirmation_ = request.POST["confirmation"]
        if password_ != confirmation_:
            return render(request, "auctions/register.html", {
                "message": "Error. Passwords are different."
            })
        try:
            usr_ = User.objects.create_user(username_, email_, password_)
            usr_.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Error. User exists."
            })
        login(request, usr_)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

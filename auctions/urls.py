from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("categories", views.categories_view, name="categories"),
    path("categories/<str:category>", views.category_listings, name="show"),
    path("watchlist", views.watchlist_view, name="watchlist"),
    path("comment", views.comment_view, name="comment"),
    path("create_listings", views.create_listings_view, name="create_listings"),
    path("active_listings", views.active_listings_view, name="active_listings"),
    path("listings", views.listings_view, name="listings"),
    path("register", views.register_view, name="register")
]
urlpatterns += staticfiles_urlpatterns()
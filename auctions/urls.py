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
    path("listing/<int:id>", views.listings_view, name="listing"),
    path("register", views.register_view, name="register")
]
urlpatterns += staticfiles_urlpatterns()

from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("categories", views.categories_view, name="categories"),
    path("categories/<str:category>", views.add_category_view, name="show"),
    path("add_watchlist/<int:id>",views.add_watchlist_view,name="add_watchlist"),
    path("watchlist", views.watchlist_view, name="watchlist"),
    path("comment/<int:id>", views.comment_view, name="comment"),
    path("create_listings", views.create_listings_view, name="create_listings"),
    path("listing/<int:id>", views.listings_view, name="listing"),
    path("register", views.register_view, name="register"),
]
urlpatterns += staticfiles_urlpatterns()

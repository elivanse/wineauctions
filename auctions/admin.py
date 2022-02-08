from django.contrib import admin

from .models import User, bid, comment, listing, watchlist

admin.site.register(listing)
admin.site.register(watchlist)
admin.site.register(comment)
admin.site.register(bid)
admin.site.register(User)


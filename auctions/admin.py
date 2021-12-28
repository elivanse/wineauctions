from django.contrib import admin
from .models import listing,watchlist,comment,bids,User
admin.site.register(listing)
admin.site.register(watchlist)
admin.site.register(comment)
admin.site.register(bids)
admin.site.register(User)


# Register your models here.

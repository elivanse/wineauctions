from django.contrib import admin
from .models import auction_lst,watchlist,comment,bids,User
admin.site.register(auction_lst)
admin.site.register(watchlist)
admin.site.register(comment)
admin.site.register(bids)
admin.site.register(User)


# Register your models here.

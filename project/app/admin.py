from django.contrib import admin
from .models import Chargingspot,Feedback,Location,Post,Reply,Reservation,User
# Register your models here.
admin.site.register(Chargingspot)
admin.site.register(Feedback)
admin.site.register(Location)
admin.site.register(Post)
admin.site.register(Reply)
admin.site.register(Reservation)
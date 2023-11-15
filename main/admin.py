from django.contrib import admin
from .models import Hotel, Room, RoomType, Booking
from .forms import BookingForm

class BookingAdmin(admin.ModelAdmin):
    form = BookingForm

admin.site.register(Hotel)
admin.site.register(Room)
admin.site.register(RoomType)
admin.site.register(Booking, BookingAdmin)

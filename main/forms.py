from django import forms
from django.contrib.auth.models import User
from django.contrib.admin.widgets import AdminDateWidget
from .models import Booking, Room

class BookingForm(forms.ModelForm):
    room = forms.ModelChoiceField(queryset=Room.objects.all(), empty_label=None)
    check_in_date = forms.DateField(widget=AdminDateWidget)
    check_out_date = forms.DateField(widget=AdminDateWidget)

    class Meta:
        model = Booking
        fields = ('user', 'room', 'check_in_date', 'check_out_date')
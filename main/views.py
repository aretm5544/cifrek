from rest_framework.views import APIView
from rest_framework import viewsets
from django.db.models import Q
from .models import Hotel, Room, RoomType, Booking
from .serializers import HotelSerializer, RoomTypeSerializer, RoomSerializer, BookingSerializer

class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

class RoomTypeViewSet(viewsets.ModelViewSet):
    queryset = RoomType.objects.all()
    serializer_class = RoomTypeSerializer
    def get_queryset(self):
        queryset = RoomType.objects.all()
        hotel_id = self.request.query_params.get('hotel_id', None)
        if hotel_id is not None:
            queryset = queryset.filter(hotel_id=hotel_id)
        return queryset

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class BookingViewSet(APIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    def get_queryset(self):
       queryset = Booking.objects.all()
       check_in_date = self.request.query_params.get('check_in_date', None)
       check_out_date = self.request.query_params.get('check_out_date', None)
       hotel_id = self.request.query_params.get('hotel_id', None)
        
        # if there are no filter conditions, return all bookings
       if check_in_date is None and check_out_date is None and hotel_id is None:
            return queryset

       filters = Q()

       if check_in_date is not None and check_out_date is not None:
            filters &= Q(check_in_date__gte=check_in_date) & Q(check_out_date__lte=check_out_date)

       if hotel_id is not None:
            filters &= Q(hotel_id=hotel_id)

       return queryset.filter(filters)





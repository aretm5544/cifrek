from rest_framework import serializers
from .models import Hotel, Room, RoomType, Booking

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'

class RoomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields = '__all__'
    
    def to_representation(self, instance):
        result = super().to_representation(instance)
        if self.context['request'].GET.get('hotel_id'):
            result['rooms'] = RoomSerializer(Room.objects.filter(room_type=instance, hotel_id=self.context['request'].GET.get('hotel_id')), many=True).data
        else:
            result['rooms'] = RoomSerializer(Room.objects.filter(room_type=instance), many=True).data
        return result

class RoomSerializer(serializers.ModelSerializer):
    room_type = RoomTypeSerializer()
    hotel = HotelSerializer()

    class Meta:
        model = Room
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    room = RoomSerializer()

    class Meta:
        model = Booking
        fields = '__all__'

from rest_framework import serializers

class BookingSerializer(serializers.Serializer):
    guest_name = serializers.CharField()
    room_number = serializers.IntegerField()
    check_in = serializers.DateField()
    check_out = serializers.DateField()

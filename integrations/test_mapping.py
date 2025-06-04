
from django.test import TestCase
from integrations.serializers import BookingSerializer

class TestBookingSerializer(TestCase):
    def test_serializer_valid_data(self):
        data = {
            "guest_name": "Jane Doe",
            "room_number": 305,
            "check_in": "2025-07-01",
            "check_out": "2025-07-05"
        }

        serializer = BookingSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data["guest_name"], "Jane Doe")

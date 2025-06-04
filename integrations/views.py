
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services.pms_client import fetch_pms_bookings
from .serializers import BookingSerializer

class BookingListView(APIView):
    def get(self, request):
        try:
            raw_bookings = fetch_pms_bookings()
            serializer = BookingSerializer(raw_bookings, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_502_BAD_GATEWAY)

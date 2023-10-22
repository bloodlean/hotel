from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import *

#Viewset
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import *

from apps.booking.models import *
from apps.guest.models import *
from apps.hotel.models import *
from apps.room.models import *

class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAdminUser]
    authentication_classes = [JWTAuthentication]

class GuestViewSet(ModelViewSet):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer
    permission_classes = [IsAdminUser]
    authentication_classes = [JWTAuthentication]

class HotelViewSet(ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    permission_classes = [IsAdminUser]
    authentication_classes = [JWTAuthentication]

class RoomViewSet(ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAdminUser]
    authentication_classes = [JWTAuthentication]


"""class BookingAPIView(APIView):

    def get(self, request):
        booking = Booking.objects.all()
        serializer = BookingSerializer(booking, many=True)
        return Response(
            serializer.data,
            status=HTTP_200_OK
        )

    def post(self, request):
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=HTTP_400_BAD_REQUEST
        )

class BookingDetailAPIView(APIView):

    def get(self, request, pk):
        booking = Booking.objects.get(pk=pk)
        serializer = BookingSerializer(booking)
        return Response(
            serializer.data,
            status=HTTP_200_OK
        )

    def patch(self, request, pk):
        booking = Booking.objects.get(pk=pk)
        serializer = BookingSerializer(booking, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=HTTP_202_ACCEPTED
            )
        return Response(
            serializer.errors,
            status=HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        booking = Booking.objects.get(pk=pk)
        booking.delete()
        return Response(status=HTTP_204_NO_CONTENT)

#Guest
class GuestAPIView(APIView):
    
    def get(self, request):
        guest = Guest.objects.all()
        serializer = GuestSerializer(guest, many=True)
        return Response(
            serializer.data,
            status=HTTP_200_OK
        )

    def post(self, request):
        serializer = GuestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=HTTP_400_BAD_REQUEST
        )

class GuestDetailAPIView(APIView):

    def get(self, request, pk):
        guest = Guest.objects.get(pk=pk)
        serializer = GuestSerializer(guest)
        return Response(
            serializer.data,
            status=HTTP_200_OK
        )

    def patch(self, request, pk):
        guest = Guest.objects.get(pk=pk)
        serializer = GuestSerializer(guest, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=HTTP_202_ACCEPTED
            )
        return Response(
            serializer.errors,
            status=HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        guest = Guest.objects.get(pk=pk)
        guest.delete()
        return Response(status=HTTP_204_NO_CONTENT)

#Hotel

class HotelAPIView(APIView):
    
    def get(self, request):
        hotel = Hotel.objects.all()
        serializer = HotelSerializer(hotel, many=True)
        return Response(
            serializer.data,
            status=HTTP_200_OK
        )

    def post(self, request):
        serializer = HotelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=HTTP_400_BAD_REQUEST
        )

class HotelDetailAPIView(APIView):

    def get(self, request, pk):
        hotel = Hotel.objects.get(pk=pk)
        serializer = HotelSerializer(hotel)
        return Response(
            serializer.data,
            status=HTTP_200_OK
        )

    def patch(self, request, pk):
        hotel = Hotel.objects.get(pk=pk)
        serializer = HotelSerializer(hotel, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=HTTP_202_ACCEPTED
            )
        return Response(
            serializer.errors,
            status=HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        hotel = Hotel.objects.get(pk=pk)
        hotel.delete()
        return Response(status=HTTP_204_NO_CONTENT)

#Room

class RoomAPIView(APIView):
    
    def get(self, request):
        room = Room.objects.all()
        serializer = RoomSerializer(room, many=True)
        return Response(
            serializer.data,
            status=HTTP_200_OK
        )

    def post(self, request):
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=HTTP_400_BAD_REQUEST
        )

class RoomDetailAPIView(APIView):

    def get(self, request, pk):
        room = Room.objects.get(pk=pk)
        serializer = HotelSerializer(room)
        return Response(
            serializer.data,
            status=HTTP_200_OK
        )

    def patch(self, request, pk):
        room = Room.objects.get(pk=pk)
        serializer = HotelSerializer(room, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=HTTP_202_ACCEPTED
            )
        return Response(
            serializer.errors,
            status=HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        room = Room.objects.get(pk=pk)
        room.delete()
        return Response(status=HTTP_204_NO_CONTENT)
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
]

router = DefaultRouter()
router.register('booking', BookingViewSet, basename='booking')
urlpatterns += router.urls

router = DefaultRouter()
router.register('guest', GuestViewSet, basename='guest')
urlpatterns += router.urls

router = DefaultRouter()
router.register('hotel', HotelViewSet, basename='hotel')
urlpatterns += router.urls

router = DefaultRouter()
router.register('room', RoomViewSet, basename='room')
urlpatterns += router.urls
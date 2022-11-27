from django.urls import path

from .views import get_chat, get_room

urlpatterns = [
    path('', get_chat, name='get_chat'),
    path('<str:room_name>/', get_room, name='get_room'),
]
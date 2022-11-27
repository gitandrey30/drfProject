from django.shortcuts import render


def get_chat(request):
    return render(request, 'chat.html')


def get_room(request, room_name):
    return render(request, 'room.html', {
        'room_name': room_name
    })

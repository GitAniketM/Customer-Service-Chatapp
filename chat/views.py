from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'chat/index.html')

@login_required
def room(request, room_name):
    print(request.user.username)
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })
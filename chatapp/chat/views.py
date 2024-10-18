from django.shortcuts import render,redirect
from .models import Room,Message
from django.http import HttpResponse, JsonResponse
# Create your views here.

def home(request):
    return render(request,'home.html')

def room(request,room):
    username=request.GET.get('username')
    roomname=Room.objects.get(name=room)
    return render(request,'room.html',{'room':room,'username':username, 'roomname':roomname})

def check(request):
    roomname=request.POST['room_name']
    username=request.POST['username']

    if Room.objects.filter(name=roomname).exists():
        return redirect('/'+roomname+'/?username='+username)
    else:
        newroom=Room.objects.create(name=roomname)
        newroom.save()
        return redirect('/'+roomname+'/?username='+username)

def send(request):
    msg=request.POST['message']
    username=request.POST['username']
    roomid=Room.objects.get(id=roomid)

    newmessage=Message.objects.create(msg=msg, user=username, room=roomid)
    newmessage.save()
    return HttpResponse("Message sent")

def getmsg(request,room):
    room_details=Room.objects.get(name=room)
    messages=Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})

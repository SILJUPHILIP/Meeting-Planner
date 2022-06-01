from django.shortcuts import render, get_object_or_404, redirect
from .models import Meetings, Room
from django.forms import modelform_factory
# Create your views here.
def detail (request, id):
    meeting = get_object_or_404(Meetings, pk = id)
    return render (request, "meeting/detail.html", {"meeting": meeting})

def room_list (request):
    rooms = Room.objects.all()
    return render (request,"meeting/room_list.html", {"rooms": rooms})

MeetingForm = modelform_factory(Meetings, exclude=[])

def new (request):
    if request.method == "POST":
        form= MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = MeetingForm()
    return render (request, "meeting/new.html", {"form": form})
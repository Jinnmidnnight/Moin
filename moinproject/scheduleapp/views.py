from django.shortcuts import render, redirect, get_object_or_404
from openapp.models import Open_1
from scheduleapp.models import Schedule_1

# Create your views here.

def schedule_make(request, open_id):
    open = get_object_or_404(Open_1, pk = open_id)
    return render(request, 'schedule_make.html', {'open' : open})

def schedule_1(request, open_id):
    open = get_object_or_404(Open_1, pk = open_id)
    return render(request, 'schedule_1.html', {'open' : open})

def schedule_making(request, open_id):
    # open = get_object_or_404(Open_1, pk = open_id)
    # return render(request, 'schedule_making.html', {'open' : open})
    if request.method == 'GET':
        return render(request, "open_1.html")
    
    schedule = Schedule_1.objects.create()
    schedule.title = request.POST['title']
    schedule.date = request.POST['date']
    schedule.location = request.POST['location']
    schedule.price = request.POST['price']
    schedule.save()
    return redirect('schedule_1', open.id)

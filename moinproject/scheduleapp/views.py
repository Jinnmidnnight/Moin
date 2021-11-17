from django.shortcuts import render, redirect, get_object_or_404
from openapp.models import Open_1
from scheduleapp.models import Schedule_1
import re

# Create your views here.

def schedule_make(request, open_id):
    open = get_object_or_404(Open_1, pk = open_id)
    return render(request, 'schedule_make.html', {'open' : open})

def schedule_1(request, open_id):
    open = get_object_or_404(Open_1, pk = open_id)
    schedules = Schedule_1.objects.all()
    return render(request, 'schedule_1.html', {'open' : open, 'schedules' : schedules})

def schedule_making_1(request, open_id):
    # open = get_object_or_404(Open_1, pk = open_id)
    # return render(request, 'schedule_making.html', {'open' : open})
    if request.method == 'GET':
        open = get_object_or_404(Open_1, pk = open_id)
        return render(request, "schedule_making_1.html", {'open':open})
    
    schedule = Schedule_1.objects.create()
    schedule.writer = request.user
    schedule.title = request.POST['title']
    
    schedule.date = request.POST['date']
    scheduleday = re.compile('[0-9]{4}-[0-9]{2}-[0-9]{2}')
    if scheduleday.match(schedule.date) != None:
         pass
    else:
        errMsg = "생년월일 양식을 지켜주세요."
        open = get_object_or_404(Open_1, pk = open_id)
        return render(request, 'schedule_making_1.html', {'open':open, 'error': errMsg})

    schedule.location = request.POST['location']
    schedule.price = request.POST['price']
    schedule.save()
    return redirect('schedule_1', open_id)

def schedule_detail_1(request, schedule_id):
    schedule = get_object_or_404(Schedule_1, pk = schedule_id)
    return render(request, 'schedule_detail_1.html', {'schedule':schedule})
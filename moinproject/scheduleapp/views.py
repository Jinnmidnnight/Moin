from django.shortcuts import render, get_object_or_404
from openapp.models import Open_1

# Create your views here.

def schedule_make(request, open_id):
    open = get_object_or_404(Open_1, pk = open_id)
    return render(request, 'schedule_make.html', {'open' : open})

def schedule_1(request, open_id):
    open = get_object_or_404(Open_1, pk = open_id)
    return render(request, 'schedule_1.html', {'open' : open})

def schedule_making(request, open_id):
    open = get_object_or_404(Open_1, pk = open_id)
    return render(request, 'schedule_making.html', {'open' : open})
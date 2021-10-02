from django.shortcuts import render, get_object_or_404
from openapp.models import Open_1

# Create your views here.

def schedule_1(request, open_id):
    open = get_object_or_404(Open_1, pk = open_id)
    return render(request, 'schedule_1.html', {'open' : open})
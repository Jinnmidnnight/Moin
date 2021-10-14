from django.shortcuts import render

# Create your views here.


def mygroup(request):
    return render(request, 'mygroup.html')

def alert(request):
    return render(request, 'alert.html')

def alert_detail(request):
    return render(request, 'alert_detail.html')

def alert_approval(request):
    return render(request, 'alert_approval.html')
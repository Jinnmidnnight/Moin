from django.shortcuts import render

# Create your views here.

def joinin_wait(request):
     return render(request,'joinin_wait.html')

def joinin(request):
     return render(request,'joinin.html')

def mygroup(request):
    return render(request, 'mygroup.html')

def alert(request):
    return render(request, 'alert.html')

def alert_detail(request):
    return render(request, 'alert_detail.html')

def alert_approval(request):
    return render(request, 'alert_approval.html')
from django.shortcuts import render, get_object_or_404, redirect
from openapp.models import Open_1, Open_2, Open_3, Open_4, Open_5, Open_6, Open_7, Open_8, Open_9

# Create your views here.

def select(request):
    return render(request, 'select.html')

def schedule(request):
    return render(request, 'schedule.html')

def open_1(request):
    if request.method == "GET":
        return render(request, "open_1.html")
    
    open = Open_1.objects.create()
    open.title = request.POST['title']
    open.intro = request.POST['intro']
    open.content = request.POST['content']
    open.image = request.FILES.get('image')
    open.number = request.POST['number']
    open.save()
    return redirect('detail_1', open.id)

def index_1(request):
    open_index = Open_1.objects.all()
    return render(request, 'index_1.html', {'open_index' : open_index})

def detail_1(request, open_id):
    open = get_object_or_404(Open_1, pk = open_id)
    return render(request, 'detail_1.html', {'open' : open})

def write_1(request):
    return render(request, 'write_1.html')

def open_2(request):
    if request.method == "GET":
        return render(request, "open_2.html")
    
    open = Open_2.objects.create()
    open.title = request.POST['title']
    open.intro = request.POST['intro']
    open.content = request.POST['content']
    open.image = request.FILES.get('image')
    open.number = request.POST['number']
    open.save()
    return redirect('detail_2', open.id)

def index_2(request):
    open_index = Open_2.objects.all()
    return render(request, 'index_2.html', {'open_index' : open_index})

def detail_2(request, open_id):
    open = get_object_or_404(Open_1, pk = open_id)
    return render(request, 'detail_2.html', {'open' : open})

def open_3(request):
    if request.method == "GET":
        return render(request, "open_3.html")
    
    open = Open_3.objects.create()
    open.title = request.POST['title']
    open.intro = request.POST['intro']
    open.content = request.POST['content']
    open.image = request.FILES.get('image')
    open.number = request.POST['number']
    open.save()
    return redirect('detail_3', open.id)

def index_3(request):
    open_index = Open_3.objects.all()
    return render(request, 'index_3.html', {'open_index' : open_index})

def detail_3(request, open_id):
    open = get_object_or_404(Open_3, pk = open_id)
    return render(request, 'detail_3.html', {'open' : open})

def open_4(request):
    if request.method == "GET":
        return render(request, "open_4.html")
    
    open = Open_4.objects.create()
    open.title = request.POST['title']
    open.intro = request.POST['intro']
    open.content = request.POST['content']
    open.image = request.FILES.get('image')
    open.number = request.POST['number']
    open.save()
    return redirect('detail_4', open.id)

def index_4(request):
    open_index = Open_4.objects.all()
    return render(request, 'index_4.html', {'open_index' : open_index})

def detail_4(request, open_id):
    open = get_object_or_404(Open_4, pk = open_id)
    return render(request, 'detail_4.html', {'open' : open})

def open_5(request):
    if request.method == "GET":
        return render(request, "open_5.html")
    
    open = Open_5.objects.create()
    open.title = request.POST['title']
    open.intro = request.POST['intro']
    open.content = request.POST['content']
    open.image = request.FILES.get('image')
    open.number = request.POST['number']
    open.save()
    return redirect('detail_5', open.id)

def index_5(request):
    open_index = Open_5.objects.all()
    return render(request, 'index_5.html', {'open_index' : open_index})

def detail_5(request, open_id):
    open = get_object_or_404(Open_5, pk = open_id)
    return render(request, 'detail_5.html', {'open' : open})

def open_6(request):
    if request.method == "GET":
        return render(request, "open_6.html")
    
    open = Open_6.objects.create()
    open.title = request.POST['title']
    open.intro = request.POST['intro']
    open.content = request.POST['content']
    open.image = request.FILES.get('image')
    open.number = request.POST['number']
    open.save()
    return redirect('detail_6', open.id)

def index_6(request):
    open_index = Open_6.objects.all()
    return render(request, 'index_6.html', {'open_index' : open_index})

def detail_6(request, open_id):
    open = get_object_or_404(Open_6, pk = open_id)
    return render(request, 'detail_6.html', {'open' : open})

def open_7(request):
    if request.method == "GET":
        return render(request, "open_7.html")
    
    open = Open_7.objects.create()
    open.title = request.POST['title']
    open.intro = request.POST['intro']
    open.content = request.POST['content']
    open.image = request.FILES.get('image')
    open.number = request.POST['number']
    open.save()
    return redirect('detail_7', open.id)

def index_7(request):
    open_index = Open_7.objects.all()
    return render(request, 'index_7.html', {'open_index' : open_index})

def detail_7(request, open_id):
    open = get_object_or_404(Open_7, pk = open_id)
    return render(request, 'detail_7.html', {'open' : open})

def open_8(request):
    if request.method == "GET":
        return render(request, "open_8.html")
    
    open = Open_8.objects.create()
    open.title = request.POST['title']
    open.intro = request.POST['intro']
    open.content = request.POST['content']
    open.image = request.FILES.get('image')
    open.number = request.POST['number']
    open.save()
    return redirect('detail_8', open.id)

def index_8(request):
    open_index = Open_8.objects.all()
    return render(request, 'index_8.html', {'open_index' : open_index})

def detail_8(request, open_id):
    open = get_object_or_404(Open_8, pk = open_id)
    return render(request, 'detail_8.html', {'open' : open})

def open_9(request):
    if request.method == "GET":
        return render(request, "open_9.html")
    
    open = Open_9.objects.create()
    open.title = request.POST['title']
    open.intro = request.POST['intro']
    open.content = request.POST['content']
    open.image = request.FILES.get('image')
    open.number = request.POST['number']
    open.save()
    return redirect('detail_9', open.id)

def index_9(request):
    open_index = Open_9.objects.all()
    return render(request, 'index_9.html', {'open_index' : open_index})

def detail_9(request, open_id):
    open = get_object_or_404(Open_9, pk = open_id)
    return render(request, 'detail_9.html', {'open' : open})
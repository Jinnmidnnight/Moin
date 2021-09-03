from django.shortcuts import render, get_object_or_404, redirect
from openapp_1.models import Open_1

# Create your views here.

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
    love = get_object_or_404(Open_1, pk = open_id)
    return render(request, 'detail_1.html', {'open' : open})

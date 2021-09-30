from django.shortcuts import render, get_object_or_404, redirect
from openapp.models import Open_1, Open_2, Open_3, Open_4, Open_5, Open_6, Open_7, Open_8, Open_9
from .models import Write_1
from .forms import WriteForm_1

# Create your views here.

def write_1(request, open_id):
    open = get_object_or_404(Open_1, pk = open_id)
    if request.method == "POST":
        form = WriteForm_1(request.POST, request.FILES)
        if form.is_valid():
            write = form.save(commit = False)
            write.post = open
            write.save()
        return redirect('detail_1', open_id)
    else:
        form = WriteForm_1()
        return render(request, "write_1.html", {'form' : form})
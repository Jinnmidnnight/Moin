from django.shortcuts import render, get_object_or_404, redirect
from openapp.models import Open_1, Open_2, Open_3, Open_4, Open_5, Open_6, Open_7, Open_8, Open_9
from .models import Write_1, Write_2, Write_3, Write_4, Write_5, Write_6, Write_7, Write_8, Write_9
from .forms import WriteForm_1, WriteForm_2, WriteForm_3, WriteForm_4, WriteForm_5, WriteForm_6, WriteForm_7, WriteForm_8, WriteForm_9, Commentform_1

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

def comment_1(request, write_id):
    write = get_object_or_404(Write_1, pk = write_id)
    if request.method == "POST":
        form = Commentform_1(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.post = write
            comment.save()
        return redirect('write_1', write_id)
    else:
        form = Commentform_1()
        return render(request, 'comment_1.html', {'form' : form})

def write_2(request, open_id):
    open = get_object_or_404(Open_2, pk = open_id)
    if request.method == "POST":
        form = WriteForm_2(request.POST, request.FILES)
        if form.is_valid():
            write = form.save(commit = False)
            write.post = open
            write.save()
        return redirect('detail_2', open_id)
    else:
        form = WriteForm_2()
        return render(request, "write_2.html", {'form' : form})

def comment_2(request, write_id):
    write = get_object_or_404(Write_2, pk = write_id)
    return render(request, 'comment_2.html', {'write' : write})

def write_3(request, open_id):
    open = get_object_or_404(Open_3, pk = open_id)
    if request.method == "POST":
        form = WriteForm_3(request.POST, request.FILES)
        if form.is_valid():
            write = form.save(commit = False)
            write.post = open
            write.save()
        return redirect('detail_3', open_id)
    else:
        form = WriteForm_3()
        return render(request, "write_3.html", {'form' : form})

def comment_3(request, write_id):
    write = get_object_or_404(Write_3, pk = write_id)
    return render(request, 'comment_3.html', {'write' : write})

def write_4(request, open_id):
    open = get_object_or_404(Open_4, pk = open_id)
    if request.method == "POST":
        form = WriteForm_4(request.POST, request.FILES)
        if form.is_valid():
            write = form.save(commit = False)
            write.post = open
            write.save()
        return redirect('detail_4', open_id)
    else:
        form = WriteForm_4()
        return render(request, "write_4.html", {'form' : form})

def comment_4(request, write_id):
    write = get_object_or_404(Write_4, pk = write_id)
    return render(request, 'comment_4.html', {'write' : write})

def write_5(request, open_id):
    open = get_object_or_404(Open_5, pk = open_id)
    if request.method == "POST":
        form = WriteForm_5(request.POST, request.FILES)
        if form.is_valid():
            write = form.save(commit = False)
            write.post = open
            write.save()
        return redirect('detail_5', open_id)
    else:
        form = WriteForm_5()
        return render(request, "write_5.html", {'form' : form})

def comment_5(request, write_id):
    write = get_object_or_404(Write_5, pk = write_id)
    return render(request, 'comment_5.html', {'write' : write})

def write_6(request, open_id):
    open = get_object_or_404(Open_6, pk = open_id)
    if request.method == "POST":
        form = WriteForm_6(request.POST, request.FILES)
        if form.is_valid():
            write = form.save(commit = False)
            write.post = open
            write.save()
        return redirect('detail_6', open_id)
    else:
        form = WriteForm_6()
        return render(request, "write_6.html", {'form' : form})

def comment_6(request, write_id):
    write = get_object_or_404(Write_6, pk = write_id)
    return render(request, 'comment_6.html', {'write' : write})

def write_7(request, open_id):
    open = get_object_or_404(Open_7, pk = open_id)
    if request.method == "POST":
        form = WriteForm_7(request.POST, request.FILES)
        if form.is_valid():
            write = form.save(commit = False)
            write.post = open
            write.save()
        return redirect('detail_7', open_id)
    else:
        form = WriteForm_7()
        return render(request, "write_7.html", {'form' : form})

def comment_7(request, write_id):
    write = get_object_or_404(Write_7, pk = write_id)
    return render(request, 'comment_7.html', {'write' : write})

def write_8(request, open_id):
    open = get_object_or_404(Open_8, pk = open_id)
    if request.method == "POST":
        form = WriteForm_8(request.POST, request.FILES)
        if form.is_valid():
            write = form.save(commit = False)
            write.post = open
            write.save()
        return redirect('detail_8', open_id)
    else:
        form = WriteForm_8()
        return render(request, "write_8.html", {'form' : form})

def comment_8(request, write_id):
    write = get_object_or_404(Write_8, pk = write_id)
    return render(request, 'comment_8.html', {'write' : write})

def write_9(request, open_id):
    open = get_object_or_404(Open_9, pk = open_id)
    if request.method == "POST":
        form = WriteForm_9(request.POST, request.FILES)
        if form.is_valid():
            write = form.save(commit = False)
            write.post = open
            write.save()
        return redirect('detail_9', open_id)
    else:
        form = WriteForm_9()
        return render(request, "write_9.html", {'form' : form})

def comment_9(request, write_id):
    write = get_object_or_404(Write_9, pk = write_id)
    return render(request, 'comment_9.html', {'write' : write})
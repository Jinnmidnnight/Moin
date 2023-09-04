from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from account.models import User
from .models import Open_1, Write_1, Comment_1
from .forms import WriteForm_1, Commentform_1

@login_required(login_url='login')
def open_1(request):
    if request.method == "GET":
        return render(request, "open_1.html")

    open = Open_1.objects.create()
    open.writer = request.user
    open.title = request.POST['title']
    open.intro = request.POST['intro']
    open.content = request.POST['content']
    open.image = request.FILES.get('image')
    open.number = request.POST['number']
    open.save()
    return redirect('detail_1', open.id)

def index_1(request):
    open_index = Open_1.objects.all().order_by('-created_at')
    return render(request,'index_1.html',{'open_index' : open_index})

def index_1_1(request):
    open_index = Open_1.objects.all().order_by('-like_count','-created_at')
    return render(request,'index_1_1.html',{'open_index' : open_index})

def detail_1(request, open_id):
    open = get_object_or_404(Open_1, pk = open_id)
    user_id = request.session.get('user')
    if user_id:
        user = User.objects.get(pk = user_id)
        return render(request, 'detail_1.html', {'user': user})
    else:
        return render(request, 'detail_1.html', {'open' : open})

@login_required(login_url='login')
def likes_1(request, open_id):
    like_b = get_object_or_404(Open_1, id=open_id)
    if request.user in like_b.like.all():
        like_b.like.remove(request.user)
        like_b.like_count -= 1
        like_b.save()
    else:
        like_b.like.add(request.user)
        like_b.like_count += 1
        like_b.save()
    return redirect('detail_1', open_id)

def follow_1(request, open_id):
    open = get_object_or_404(Open_1, id=open_id)
    if request.user in open.follower.all():
        open.follower.remove(request.user)
        open.follower_count -= 1
        open.save()
    else:
        if open.follower_count < open.number:
            open.follower.add(request.user)
            open.follower_count += 1
            open.save()
        else:
            return redirect('detail_1', open_id)
    return redirect('detail_1', open_id)

@csrf_exempt
def write_1(request, open_id):
    open = get_object_or_404(Open_1, pk = open_id)
    if request.method == "POST":
        form = WriteForm_1(request.POST, request.FILES)
        if form.is_valid():
            write = form.save(commit = False)
            write.author = request.user
            write.post = open
            write.save()
        return redirect('detail_1', open_id)
    else:
        form = WriteForm_1()
        return render(request, "write_1.html", {'form' : form})

def comment_1(request, write_id):
    write = get_object_or_404(Write_1, pk = write_id)
    form = Commentform_1()
    return render(request, 'comment_1.html', {'write': write, 'form': form})

@csrf_exempt
def add_comment_1(request, write_id):
    form = Commentform_1(request.POST)
    if form.is_valid():
        write = get_object_or_404(Write_1, pk=write_id)
        write.comment_count += 1
        write.save()
        finished_form = form.save(commit=False)
        finished_form.reply = request.user
        finished_form.post = get_object_or_404(Write_1, pk=write_id)
        finished_form.save()
    return redirect('comment_1', write_id)

def write_like_1(request, write_id):
    like_b = get_object_or_404(Write_1, id=write_id)
    if request.user in like_b.write_like.all():
        like_b.write_like.remove(request.user)
        like_b.write_like_count -= 1
        like_b.save()
    else:
        like_b.write_like.add(request.user)
        like_b.write_like_count += 1
        like_b.save()
    return redirect('comment_1', write_id)

def update_1(request, open_id):
    if request.method == "GET":
        open = get_object_or_404(Open_1, pk = open_id)
        return render(request, "update_1.html", {"open": open})

    open = get_object_or_404(Open_1, pk = open_id)
    open.title = request.POST['title']
    open.intro = request.POST['intro']
    open.content = request.POST['content']
    open.image = request.FILES.get('image')
    open.number = request.POST['number']
    open.save()
    return redirect('detail_1', open.id)

def delete_alert_1(request, open_id):
    open = get_object_or_404(Open_1, pk = open_id)
    return render(request, "delete_alert_1.html", {"open": open})

def delete_1(request, open_id):
    open = get_object_or_404(Open_1, pk = open_id)
    open.delete()
    return redirect('index_1')

@csrf_exempt
def write_update_1(request, open_id, write_id):
    open = get_object_or_404(Open_1, pk=open_id)
    my_write = get_object_or_404(Write_1, pk=write_id)

    if request.method == "POST":
        form = WriteForm_1(request.POST, request.FILES, instance=my_write)
        if form.is_valid():
            write = form.save(commit = False)
            write.author = request.user
            write.post = open
            write.save()
        return redirect('detail_1', open_id)
    else:
        return render(request, 'write_update_1.html', {'my_write': my_write})

def write_delete_1(request, write_id):
    write = get_object_or_404(Write_1, pk=write_id)
    post = get_object_or_404(Open_1, pk = write.post.id)
    
    write.delete()
   
    return redirect('detail_1', post.id)

def comment_delete_1(request, comment_id):
    comment = get_object_or_404(Comment_1, pk=comment_id)
    post = get_object_or_404(Write_1, pk = comment.post.id)
    post.comment_count -= 1
    post.save()

    comment.delete()
    return redirect('comment_1', post.id)

def deport_alert_1(request, open_id):
    open = get_object_or_404(Open_1, pk = open_id)
    user_id = request.session.get('user')
    if user_id:
        user = User.objects.get(pk = user_id)
        return render(request, 'deport_alert_1.html', {'user': user})
    else:
        return render(request, 'deport_alert_1.html', {'open' : open})

def deport_1(request, open_id):
    open = get_object_or_404(Open_1, id=open_id)

    open.follower.clear()
    open.follower_count = 1
    open.save()
    return redirect('detail_1', open_id)


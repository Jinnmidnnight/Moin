from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from account.models import User
from .models import Open_5, Write_5, Comment_5
from .forms import WriteForm_5, Commentform_5

@login_required(login_url='login')
def open_5(request):
    if request.method == "GET":
        return render(request, "open_5.html")

    open = Open_5.objects.create()
    open.writer = request.user
    open.title = request.POST['title']
    open.intro = request.POST['intro']
    open.content = request.POST['content']
    open.image = request.FILES.get('image')
    open.number = request.POST['number']
    open.save()
    return redirect('detail_5', open.id)

def index_5(request):
    open_index = Open_5.objects.all().order_by('-created_at')
    return render(request,'index_5.html',{'open_index' : open_index})

def index_5_1(request):
    open_index = Open_5.objects.all().order_by('-like_count','-created_at')
    return render(request,'index_5_1.html',{'open_index' : open_index})

def detail_5(request, open_id):
    open = get_object_or_404(Open_5, pk = open_id)
    user_id = request.session.get('user')
    if user_id:
        user = User.objects.get(pk = user_id)
        return render(request, 'detail_5.html', {'user': user})
    else:
        return render(request, 'detail_5.html', {'open' : open})

@login_required(login_url='login')
def likes_5(request, open_id):
    like_b = get_object_or_404(Open_5, id=open_id)
    if request.user in like_b.like.all():
        like_b.like.remove(request.user)
        like_b.like_count -= 1
        like_b.save()
    else:
        like_b.like.add(request.user)
        like_b.like_count += 1
        like_b.save()
    return redirect('detail_5', open_id)

def follow_5(request, open_id):
    open = get_object_or_404(Open_5, id=open_id)
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
            return redirect('detail_5', open_id)
    return redirect('detail_5', open_id)

@csrf_exempt
def write_5(request, open_id):
    open = get_object_or_404(Open_5, pk = open_id)
    if request.method == "POST":
        form = WriteForm_5(request.POST, request.FILES)
        if form.is_valid():
            write = form.save(commit = False)
            write.author = request.user
            write.post = open
            write.save()
        return redirect('detail_5', open_id)
    else:
        form = WriteForm_5()
        return render(request, "write_5.html", {'form' : form})

def comment_5(request, write_id):
    write = get_object_or_404(Write_5, pk = write_id)
    form = Commentform_5()
    return render(request, 'comment_5.html', {'write': write, 'form': form})

@csrf_exempt
def add_comment_5(request, write_id):
    form = Commentform_5(request.POST)
    if form.is_valid():
        write = get_object_or_404(Write_5, pk=write_id)
        write.comment_count += 1
        write.save()
        finished_form = form.save(commit=False)
        finished_form.reply = request.user
        finished_form.post = get_object_or_404(Write_5, pk=write_id)
        finished_form.save()
    return redirect('comment_5', write_id)

def write_like_5(request, write_id):
    like_b = get_object_or_404(Write_5, id=write_id)
    if request.user in like_b.write_like.all():
        like_b.write_like.remove(request.user)
        like_b.write_like_count -= 1
        like_b.save()
    else:
        like_b.write_like.add(request.user)
        like_b.write_like_count += 1
        like_b.save()
    return redirect('comment_5', write_id)

def update_5(request, open_id):
    if request.method == "GET":
        open = get_object_or_404(Open_5, pk = open_id)
        return render(request, "update_5.html", {"open": open})

    open = get_object_or_404(Open_5, pk = open_id)
    open.title = request.POST['title']
    open.intro = request.POST['intro']
    open.content = request.POST['content']
    open.image = request.FILES.get('image')
    open.number = request.POST['number']
    open.save()
    return redirect('detail_5', open.id)

def delete_alert_5(request, open_id):
    open = get_object_or_404(Open_5, pk = open_id)
    return render(request, "delete_alert_5.html", {"open": open})

def delete_5(request, open_id):
    open = get_object_or_404(Open_5, pk = open_id)
    open.delete()
    return redirect('index_5')

@csrf_exempt
def write_update_5(request, open_id, write_id):
    open = get_object_or_404(Open_5, pk=open_id)
    my_write = get_object_or_404(Write_5, pk=write_id)

    if request.method == "POST":
        form = WriteForm_5(request.POST, request.FILES, instance=my_write)
        if form.is_valid():
            write = form.save(commit = False)
            write.author = request.user
            write.post = open
            write.save()
        return redirect('detail_5', open_id)
    else:
        return render(request, 'write_update_5.html', {'my_write': my_write})

def write_delete_5(request, write_id):
    write = get_object_or_404(Write_5, pk=write_id)
    post = get_object_or_404(Open_5, pk = write.post.id)
    
    write.delete()
   
    return redirect('detail_5', post.id)

def comment_delete_5(request, comment_id):
    comment = get_object_or_404(Comment_5, pk=comment_id)
    post = get_object_or_404(Write_5, pk = comment.post.id)
    post.comment_count -= 1
    post.save()

    comment.delete()
    return redirect('comment_5', post.id)

def deport_alert_5(request, open_id):
    open = get_object_or_404(Open_5, pk = open_id)
    user_id = request.session.get('user')
    if user_id:
        user = User.objects.get(pk = user_id)
        return render(request, 'deport_alert_5.html', {'user': user})
    else:
        return render(request, 'deport_alert_5.html', {'open' : open})

def deport_5(request, open_id):
    open = get_object_or_404(Open_5, id=open_id)

    open.follower.clear()
    open.follower_count = 1
    open.save()
    return redirect('detail_5', open_id)


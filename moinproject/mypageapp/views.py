from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import auth
from account.models import User
from writeapp.models import Write_1
from openapp.models import Open_1
# Create your views here.
def joinin_wait(request, open_id):
    open = get_object_or_404(Open_1, pk = open_id)
    return render(request, 'joinin_wait.html', {'open' : open})

def joinin(request, open_id):
    open = get_object_or_404(Open_1, pk = open_id)
    return render(request, 'joinin.html', {'open' : open})

def delete_1(request, open_id):
    open = get_object_or_404(Open_1, pk = open_id)
    open.delete()
    return redirect('mypage')

def write_delete_1(request, write_id):

    write = get_object_or_404(Write_1, pk=write_id)
    post = get_object_or_404(Open_1, pk = write.post.id)
    
    write.delete()
   
    return redirect('manage_1', post.id)

def deport_1(request, open_id):
    open = get_object_or_404(Open_1, pk = open_id)
    return render(request, 'deport_1.html', {'open' : open})

def manage_1(request, open_id):
    open = get_object_or_404(Open_1, pk = open_id)
    return render(request, 'manage_1.html', {'open' : open})

def manage_2(request, open_id):
    open = get_object_or_404(Open_1, pk = open_id)
    return render(request, 'manage_2.html', {'open' : open})

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
    return redirect('manage_1', open.id)

def mypage(request):
    open_index = Open_1.objects.all()
    user_id = request.session.get('user')
    if user_id:
        user = User.objects.get(pk = user_id)
        return render(request, 'mypage.html', {'user': user, 'open_index' : open_index})
    return render(request, 'mypage.html')

def logout(request):
    auth.logout(request)
    return redirect('home')


    
        # user1 = User.objects.create()
        # user1.자기소개 = request.POST['성별']
        # user1.save()
        # if request.method == "POST":
        #     user.자기소개 = request.POST['자기소개']
        #     user.save()
        #     return render(request, 'mypage.html', {'user': user})
        # return render(request, 'edit.html', {'user': user})
    
    # user_id = request.session.get('user')

    # 자기소개 = request.POST['자기소개']
    # 자기소개.save()

    # if user_id:
    #     user = User.objects.get(pk = user_id)

    #     return render(request, 'edit.html', {'user': user})

    # # user_change_form = UserChangeForm(instance = request.user)
    # # return render(request, 'edit.html', {'user_change_form': user_change_form})

    # return render(request, 'edit.html')

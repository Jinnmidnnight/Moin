from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import auth
from account.models import User
# Create your views here.

def mypage(request):
    user_id = request.session.get('user')
    if user_id:
        user = User.objects.get(pk = user_id)
        return render(request, 'mypage.html', {'user': user})
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

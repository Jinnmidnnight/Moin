from django.shortcuts import render, redirect
from django.contrib import auth
# from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_str
from .tokens import account_activation_token
from django.contrib.auth.hashers import check_password
from .models import User
from .forms import RegisterForm
import re
from django.contrib.auth.decorators import login_required
from moin_1.models import Open_1
from moin_2.models import Open_2
from moin_3.models import Open_3
from moin_4.models import Open_4
from moin_5.models import Open_5
from moin_6.models import Open_6
from moin_7.models import Open_7
from moin_8.models import Open_8
from moin_9.models import Open_9


def signup(request):
    form = RegisterForm()
    if request.method == "POST":
        
        errMsg = {}

        email = request.POST.get('email', None)
        try:
           User.objects.get(email = email)
           errMsg = "Email has already been used. Please use another email."
           return render(request, 'signup.html', {'form':form, 'error': errMsg})
        except:
            pass

        email = request.POST["email"]
        if "@yonsei.ac.kr" not in email:
            errMsg = "연세 메일로 가입해주세요."
            return render(request, 'signup.html', {'form':form, 'error': errMsg})

        birthday = re.compile('[0-9]{4}-[0-9]{2}-[0-9]{2}')
        birth = request.POST["생년월일"]
        if birthday.match(birth) != None:
             pass
        else:
            errMsg = "생년월일 양식을 지켜주세요."
            return render(request, 'signup.html', {'form':form, 'error': errMsg})


        if request.POST["password1"] == request.POST["password2"]:

            user = User.objects.create_user(username=request.POST["username"], email=request.POST["email"], password=request.POST["password1"], 성별=request.POST["성별"], 생년월일=request.POST["생년월일"])
            user.is_active = False
            user.save()
            current_site = get_current_site(request) 
            message = render_to_string('activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            mail_title = "계정 활성화 확인 이메일"
            mail_to = request.POST["email"]
            email = EmailMessage(mail_title, message, to=[mail_to])
            email.send()
            return redirect("home")

        else:
            errMsg = "Passwords do not match. Please check it again."
            return render(request, 'signup.html', {'form':form, 'error': errMsg})
            
    else:
        return render(request, 'signup.html', {'form':form})

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    elif request.method == 'POST':
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        errMsg = {}

        try:
            user = User.objects.get(email = email)
        except:
            errMsg['error'] = "Unregistered email."
            return render(request, 'login.html', errMsg)


        # user = User.objects.get(username = username)

        if not (email and password):
            errMsg['error'] = "Please fill in all the columns."

        # elif (user.is_active == False):
        #     errMsg['error'] = "Please check your email to activate your account."

        else:
            if check_password(password, user.password):
                if (user.is_active == False):
                    errMsg['error'] = "Please check your email to activate your account."
                    return render(request, 'login.html', errMsg)

                else:
                    auth.login(request, user)
                    # request.session['user'] = user.id
                # login(request, user)
                    return redirect('home')

            else:
                errMsg['error'] = "Password does not match."
        return render(request, 'login.html', errMsg)

def logout(request):
    auth.logout(request)
    return redirect('home')

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExsit):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        auth.login(request, user)
        return redirect('home')
    else:
        return render(request, 'home.html', {'error' : '계정 활성화 오류'})

@login_required(login_url='login')
def edit(request):
    open_1 = Open_1.objects.all()
    open_2 = Open_2.objects.all()
    open_3 = Open_3.objects.all()
    open_4 = Open_4.objects.all()
    open_5 = Open_5.objects.all()
    open_6 = Open_6.objects.all()
    open_7 = Open_7.objects.all()
    open_8 = Open_8.objects.all()
    open_9 = Open_9.objects.all()

    user = request.user

    if request.method == "POST":

        try:
            request.FILES['image']
            user.image = request.FILES['image']
            user.자기소개 = request.POST['자기소개']

        except:
            user.자기소개 = request.POST['자기소개']

        user.save()
        return render(request, 'mypage.html', {'user': user, 'open_1': open_1, 'open_2': open_2, 'open_3': open_3, 'open_4': open_4, 'open_5': open_5, 'open_6': open_6, 'open_7': open_7, 'open_8': open_8, 'open_9': open_9})

    return render(request, 'edit.html', {'user': user})

def personalinfo(request):
    return render(request, 'personalinfo.html')

def member_del(request):
	if request.method == "POST":
		pw_del = request.POST["pw_del"]
		user = request.user
		if check_password(pw_del, user.password):
			user.delete()
			return redirect('/')
	return render(request, 'member_del.html')